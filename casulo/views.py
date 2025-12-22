# Standard Library
from pathlib import Path

# Django Core
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

# Local Imports
from .forms import MensagemEditForm, MensagemForm
from .models import Mensagem, Service, ServiceCategory, TeamMember


# --- Helpers ---
def _get_espaco_images():
    """
    Retrieves a list of image filenames from the static 'espaco' directory.
    """
    espaco_dir = Path(settings.BASE_DIR) / "static" / "images" / "espaco"
    allowed = {".jpg", ".jpeg", ".png", ".webp"}

    if espaco_dir.exists():
        return sorted(
            [f.name for f in espaco_dir.iterdir()
             if f.is_file() and f.suffix.lower() in allowed]
        )
    return []


# --- Public Views ---

def landpage(request):
    """
    Main landing page view.
    Handles the contact form submission and displays services and gallery.
    """
    # 1. Load gallery images
    espaco_images = _get_espaco_images()

    # 2. Filtering logic for services
    active = request.GET.get("cat", "all")
    categories = ServiceCategory.objects.filter(is_active=True).order_by("order", "name")
    
    services = (
        Service.objects
        .filter(is_active=True, category__is_active=True)
        .select_related("category")
        .order_by("order", "title")
    )

    if active != "all":
        services = services.filter(category__slug=active)

    # 3. Load team members
    team = TeamMember.objects.filter(is_active=True).order_by("ordem", "nome")

    # 4. Handle Contact Form
    is_htmx = request.headers.get("HX-Request") == "true"
    
    if request.method == "POST":
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada com sucesso!")
            
            if is_htmx:
                # Return a fresh form for HTMX requests
                form = MensagemForm()
                return render(request, "partials/contact_form.html", {"form": form})
            
            return redirect(f"{reverse('landpage')}#contato")
            
        # Form invalid
        if is_htmx:
             return render(request, "partials/contact_form.html", {"form": form})
    else:
        form = MensagemForm()

    context = {
        "form": form,
        "categories": categories,
        "services": services,
        "active_cat": active,
        "espaco_images": espaco_images,
        "team": team,
    }

    return render(request, "landpage.html", context)


def services_partial(request):
    """
    HTMX partial view for filtering services grid.
    """
    active = request.GET.get("cat", "all")

    services = (
        Service.objects
        .filter(is_active=True, category__is_active=True)
        .select_related("category")
        .order_by("order", "title")
    )

    if active != "all":
        services = services.filter(category__slug=active)

    return render(request, "partials/services_grid.html", {
        "services": services,
        "active_cat": active,
    })


# --- Authentication & Admin Views ---

def logout_confirm(request):
    """
    Custom logout confirmation page.
    """
    if request.method == "POST":
        logout(request)
        return redirect("landpage")
    return render(request, "logout_confirm.html")


@ensure_csrf_cookie
@login_required
def messages_list(request):
    """
    Admin view to list messages with filtering and search.
    """
    status = request.GET.get("status", "all")
    q = (request.GET.get("q") or "").strip()
    data_envio = request.GET.get("data_envio")

    qs = Mensagem.objects.all()

    # Filters
    if data_envio:
        qs = qs.filter(data_envio__date=data_envio)

    if status == "unread":
        qs = qs.filter(lido=False)
    elif status == "read":
        qs = qs.filter(lido=True)

    if q:
        qs = qs.filter(Q(nome__icontains=q) | Q(email__icontains=q))

    context = {
        "mensagens": qs,
        "status": status,
        "q": q,
        "data_envio": data_envio
    }

    if request.headers.get("HX-Request") == "true":
        return render(request, "partials/messages_ul.html", context)

    return render(request, "messages_list.html", context)


@login_required
def message_detail(request, pk):
    msg = get_object_or_404(Mensagem, pk=pk)
    return render(request, "message_detail.html", {"msg": msg})


@login_required
def message_edit(request, pk):
    msg = get_object_or_404(Mensagem, pk=pk)

    if request.method == "POST":
        form = MensagemEditForm(request.POST, instance=msg)
        if form.is_valid():
            form.save()
            return redirect("message_detail", pk=msg.pk)
    else:
        form = MensagemEditForm(instance=msg)

    return render(request, "message_edit.html", {"form": form, "msg": msg})


@login_required
def message_delete_confirm(request, pk):
    msg = get_object_or_404(Mensagem, pk=pk)

    if request.method == "POST":
        msg.delete()
        return redirect("messages_list")

    return render(request, "message_delete_confirm.html", {"msg": msg})


@require_POST
@login_required
def message_toggle_read(request, pk):
    """
    Toggle the 'read' status of a message.
    Supports HTMX for optimistic UI updates/row removal.
    """
    m = get_object_or_404(Mensagem, pk=pk)
    m.lido = not m.lido
    m.save(update_fields=["lido"])

    is_htmx = request.headers.get("HX-Request") == "true"
    if not is_htmx:
        return redirect("messages_list")

    status = request.GET.get("status") or "all"
    variant = request.GET.get("variant")

    if (status == "unread" and m.lido) or (status == "read" and not m.lido):
        resp = HttpResponse("")
        resp["HX-Reswap"] = "delete"
        return resp

    return render(
        request,
        "partials/message_row.html",
        {"m": m, "status": status, "variant": variant},
    )
