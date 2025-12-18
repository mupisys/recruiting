from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Mensagem


def landpage(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        
        Mensagem.objects.create(
            nome=nome,
            email=email,
            mensagem=mensagem
        )
        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('landpage')
    
    return render(request, 'landpage.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('messages_list')
        else:
            messages.error(request, 'Usuário ou senha incorretos!')
    
    return render(request, 'login.html')

@login_required
def messages_list(request):
    mensagens = Mensagem.objects.all().order_by('-data_envio')
    total = mensagens.count()
    lidas = mensagens.filter(lido=True).count()
    nao_lidas = mensagens.filter(lido=False).count()
    
    context = {
        'mensagens': mensagens,
        'total': total,
        'lidas': lidas,
        'nao_lidas': nao_lidas,
    }
    return render(request, 'messages_list.html', context)

@login_required
def message_detail(request, pk):
    mensagem = get_object_or_404(Mensagem, pk=pk)
    return render(request, 'message_detail.html', {'mensagem': mensagem})

@login_required
def message_edit(request, pk):
    mensagem = get_object_or_404(Mensagem, pk=pk)
    
    if request.method == 'POST':
        mensagem.nome = request.POST.get('nome')
        mensagem.email = request.POST.get('email')
        mensagem.mensagem = request.POST.get('mensagem')
        mensagem.save()
        messages.success(request, 'Mensagem atualizada com sucesso!')
        return redirect('messages_list')
    
    return render(request, 'message_edit.html', {'mensagem': mensagem})

@login_required
def message_delete(request, pk):
    mensagem = get_object_or_404(Mensagem, pk=pk)
    
    if request.method == 'POST':
        mensagem.delete()
        messages.success(request, 'Mensagem excluída com sucesso!')
        return redirect('messages_list')
    
    return render(request, 'message_delete_confirm.html', {'mensagem': mensagem})

@login_required
@require_POST
def marcar_lida(request, pk):
    mensagem = get_object_or_404(Mensagem, pk=pk)

    # Toggle
    mensagem.lido = not mensagem.lido
    mensagem.save(update_fields=['lido'])

    response = render(
        request,
        'partials/botao_lida.html',
        {'mensagem': mensagem}
    )

    # ✅ EVENTO SIMPLES (FORMA CORRETA)
    response['HX-Trigger'] = 'atualizarContadores'

    return response


@login_required
def contadores(request):
    total = Mensagem.objects.count()
    lidas = Mensagem.objects.filter(lido=True).count()
    nao_lidas = Mensagem.objects.filter(lido=False).count()

    return render(request, 'partials/contadores.html', {
        'total': total,
        'lidas': lidas,
        'nao_lidas': nao_lidas
    })



# ==========================
# Fallback sem HTMX
# ==========================
@login_required
def message_toggle_read(request, pk):
    mensagem = get_object_or_404(Mensagem, pk=pk)
    mensagem.lido = not mensagem.lido
    mensagem.save(update_fields=['lido'])
    return redirect('messages_list')


# ==========================
# Logout com confirmação
# ==========================
@login_required
def logout_confirm(request):
    if request.method == 'POST':
        logout(request)
        return redirect('landpage')

    return render(request, 'logout_confirm.html')