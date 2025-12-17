from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q

from .forms import MensagemForm
from .models import Mensagem

def landpage(request):
    if request.method == "POST":
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada com sucesso!")
            return redirect("landpage")
    else:
        form = MensagemForm()

    return render(request, "landpage.html", {"form": form})

def logout_confirm(request):
    if request.method == "POST":
        logout(request)
        return redirect("landpage")
    return render(request, "logout_confirm.html")

@ensure_csrf_cookie
@login_required
def messages_list(request):
    status = request.GET.get("status", "all")
    q = (request.GET.get("q") or "").strip()

    qs = Mensagem.objects.all()

    if status == "unread":
        qs = qs.filter(lido=False)
    elif status == "read":
        qs = qs.filter(lido=True)

    if q:
        qs = qs.filter(Q(nome__icontains=q) | Q(email__icontains=q))

    context = {"mensagens": qs, "status": status, "q": q}

    if request.headers.get("HX-Request") == "true":
        return render(request, "partials/messages_ul.html", context)

    return render(request, "messages_list.html", context)

@login_required
def message_detail(request, pk):
    msg = get_object_or_404(Mensagem, pk=pk)
    
    if not msg.lido:
        msg.lido = True
        msg.save(update_fields=['lido'])
        
    return render(request, "message_detail.html", {"msg": msg})

@login_required
def message_edit(request, pk):
    msg = get_object_or_404(Mensagem, pk=pk)

    if request.method == "POST":
        form = MensagemForm(request.POST, instance=msg)
        if form.is_valid():
            form.save()
            return redirect("message_detail", pk=msg.pk)
    else:
        form = MensagemForm(instance=msg)

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
    m = get_object_or_404(Mensagem, pk=pk)
    m.lido = not m.lido
    m.save(update_fields=["lido"])

    status = request.GET.get("status", "all")

    if (status == "unread" and m.lido) or (status == "read" and not m.lido):
        resp = HttpResponse("")
        resp["HX-Reswap"] = "delete"
        return resp

    return render(request, "partials/message_row.html", {"m": m, "status": status})