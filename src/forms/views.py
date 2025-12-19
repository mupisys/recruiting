from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpRequest
from .forms import MensagemForm
from .models import Mensagem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def landpage_view(request: HttpRequest):
    if request.method == 'POST':
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('forms:landpage')
        else:
            messages.error(request, 'Erro ao enviar mensagem. Verifique os campos.')
            context = {"form": form}
            return render(request, 'landpage.html', context)
    
    context = {
        "form": MensagemForm()
    }
    return render(request, 'landpage.html', context)

@login_required(login_url='forms:login')
def messages_list_view(request):
    context = {
        "mensagens": Mensagem.objects.all().order_by('-data_envio')
    }
    return render(request, 'messages_list.html', context)

@login_required(login_url='forms:login')
def message_detail_view(request, id):
    mensagem = get_object_or_404(Mensagem, id=id)
    # Opcional: Marcar como lida automaticamente ao abrir
    if not mensagem.lido:
        mensagem.lido = True
        mensagem.save()
    return render(request, 'message_detail.html', {'mensagem': mensagem})

@login_required(login_url='forms:login')
def message_delete_view(request: HttpRequest, id):
    mensagem = get_object_or_404(Mensagem, id=id)
    if request.method == "POST":
        mensagem.delete()
        messages.success(request, 'Mensagem excluída com sucesso.')
        return redirect('forms:mensagens')
    
    return render(request, 'message_delete_confirm.html', {'mensagem': mensagem})

@login_required(login_url='forms:login')
def message_edit_view(request: HttpRequest, id):
    mensagem = get_object_or_404(Mensagem, id=id)
    
    if request.method == "POST":
        form = MensagemForm(request.POST, instance=mensagem)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem atualizada.')
            return redirect('forms:mensagens')
    else:
        form = MensagemForm(instance=mensagem)
    
    context = {
        'form': form,
        'mensagem': mensagem
    }
    return render(request, 'message_edit.html', context)

@login_required(login_url='forms:login')
def toggle_read_view(request, id):
    mensagem = get_object_or_404(Mensagem, id=id)
    mensagem.lido = not mensagem.lido
    mensagem.save()
    return redirect('forms:mensagens')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('forms:mensagens')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout_confirm.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'As senhas não conferem.')
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
            return render(request, 'register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
        return redirect('forms:login')
        
    return render(request, 'register.html')