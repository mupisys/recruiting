from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_messages
from django.http import JsonResponse
from .models import Message
from .forms import MessageForm, MessageEditForm

def landpage(request):
    """
    View para a página inicial (landpage) com formulário de contato.
    
    Se receber POST, processa o formulário e salva a mensagem.
    Se receber GET, apenas exibe a página.
    """
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            django_messages.success(request, 'Mensagem enviada com sucesso! Entraremos em contato em breve.')
            return redirect('app_principal:landpage')
    else:
        form = MessageForm()
    
    return render(request, 'app_principal/landpage.html', {'form': form})

def login_view(request):
    """
    View para login customizado (não usa admin padrão).
    
    Autentica o usuário usando django.contrib.auth.
    Redireciona para a lista de mensagens após login bem-sucedido.
    """
    if request.user.is_authenticated:
        return redirect('app_principal:messages_list')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            django_messages.success(request, f'Bem-vindo, {user.username}!')
            return redirect('app_principal:messages_list')
        else:
            django_messages.error(request, 'Usuário ou senha incorretos.')
    
    return render(request, 'app_principal/login.html')

@login_required
def logout_view(request):
    """
    View para logout com confirmação.
    
    Se receber POST com confirmação, faz logout.
    Se receber GET, exibe página de confirmação.
    """
    if request.method == 'POST':
        logout(request)
        django_messages.success(request, 'Você foi deslogado com sucesso.')
        return redirect('app_principal:landpage')
    
    return render(request, 'app_principal/logout_confirm.html')

@login_required
def messages_list(request):
    """
    View para listar todas as mensagens (área administrativa).
    
    Exibe todas as mensagens ordenadas por data (mais recentes primeiro).
    Inclui indicadores visuais de mensagens lidas/não lidas.
    """
    all_messages = Message.objects.all()
    unread_count = Message.objects.filter(isRead=False).count()
    return render(request, 'app_principal/messages_list.html', {
        'all_messages': all_messages,
        'unread_count': unread_count
    })

@login_required
def message_detail(request, message_id):
    """
    View para exibir detalhes de uma mensagem específica.
    
    Recebe o ID da mensagem e exibe todos os seus dados.
    """
    message = get_object_or_404(Message, id=message_id)
    return render(request, 'app_principal/message_detail.html', {'message': message})

@login_required
def message_edit(request, message_id):
    """
    View para editar uma mensagem.
    
    Se receber POST, atualiza a mensagem.
    Se receber GET, exibe formulário de edição.
    """
    message = get_object_or_404(Message, id=message_id)
    
    if request.method == 'POST':
        form = MessageEditForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            django_messages.success(request, 'Mensagem atualizada com sucesso!')
            return redirect('app_principal:message_detail', message_id=message.id)
    else:
        form = MessageEditForm(instance=message)
    
    return render(request, 'app_principal/message_edit.html', {
        'form': form,
        'message': message
    })

@login_required
def message_delete(request, message_id):
    """
    View para excluir uma mensagem com confirmação.
    
    Se receber POST com confirmação, deleta a mensagem.
    Se receber GET, exibe página de confirmação.
    """
    message = get_object_or_404(Message, id=message_id)
    
    if request.method == 'POST':
        message.delete()
        django_messages.success(request, 'Mensagem excluída com sucesso!')
        return redirect('app_principal:messages_list')
    
    return render(request, 'app_principal/message_delete_confirm.html', {'message': message})

@login_required
def toggle_read(request, message_id):
    """
    View para marcar/desmarcar mensagem como lida (usando HTMX).
    
    Alterna o status isRead da mensagem sem recarregar a página.
    Retorna JSON para atualização via HTMX.
    """
    message = get_object_or_404(Message, id=message_id)
    message.isRead = not message.isRead
    message.save()
    
    return render(request, 'app_principal/partials/message_status.html', {
        'message': message
    })