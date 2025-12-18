from django.shortcuts import render
from .models import Mensagem



from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404

from django.contrib.auth import logout

def landpage(request):
    #ja salva no banco
    if request.method == "POST":
        Mensagem.objects.create(
            nome=request.POST.get("nome"),
            email=request.POST.get("email"),
            mensagem=request.POST.get("mensagem"),
        )
        return render(request, "partials/success.html")

    return render(request, "landpage.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("messages_list")

    return render(request, "login.html")

@login_required
def messages_list(request):
    mensagens = Mensagem.objects.all().order_by('-data_envio')
    return render(request, 'messages_list.html', {'mensagens': mensagens})

@login_required
def message_detail(request, pk):
    mensagem = get_object_or_404(Mensagem, pk=pk)

    if not mensagem.lido:
        mensagem.lido = True
        mensagem.save()

    return render(request, "message_detail.html", {"mensagem": mensagem})

@login_required
def message_edit(request, pk):
    mensagem = get_object_or_404(Mensagem, pk=pk)

    if request.method == "POST":
        mensagem.nome = request.POST.get("nome")
        mensagem.email = request.POST.get("email")
        mensagem.mensagem = request.POST.get("mensagem")
        mensagem.save()

        return redirect("message_detail", pk=mensagem.pk)

    return render(request, "message_edit.html", {"mensagem": mensagem})

@login_required
def message_delete_confirm(request, pk):
    mensagem = get_object_or_404(Mensagem, pk=pk)

    if request.method == "POST":
        mensagem.delete()
        return redirect("messages_list")

    return render(request, "message_delete_confirm.html", {"mensagem": mensagem})

@login_required
def logout_confirm(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")

    return render(request, "logout_confirm.html")

