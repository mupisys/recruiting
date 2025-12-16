from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

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

@login_required
def messages_list(request):
    mensagens = Mensagem.objects.all()
    context = {"mensagens": mensagens}
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
    return render(request, "message_edit.html", {"pk": pk})

@login_required
def message_delete_confirm(request, pk):
    return render(request, "message_delete_confirm.html", {"pk": pk})
