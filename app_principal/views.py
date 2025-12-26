from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages # Para exibir mensagens de erro
from django.http import HttpResponse
from .models import Message

def valida_login_adm(request):
    if request.user.is_authenticated:
        return redirect('lista_mensagens')
    
    if request.method == 'POST':
        usuario_form = request.POST.get('username')
        senha_form = request.POST.get('password')

        user = authenticate(request, username = usuario_form, password = senha_form)

        if user is not None:
            login(request, user)
            # return redirect('listagem_mensagens') lembrar antes de implementar o htmx

            url_destino = resolve_url('lista_mensagens')
            response = HttpResponse()
            response['HX-Redirect'] = url_destino
            return response
        
        else:
            html_erro = """
                <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-4" role="alert">
                    <strong class="font-bold">Erro!</strong>
                    <span class="block sm:inline">Usuário ou senha inválidos!</span>
                    
                    <span class="absolute top-0 bottom-0 right-0 px-4 py-3 cursor-pointer" onclick="this.parentElement.remove();">
                        <svg class="fill-current h-6 w-6 text-red-500" role="button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                            <title>Fechar</title>
                            <path d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"/>
                        </svg>
                    </span>
                </div>
            """
            return HttpResponse(html_erro)
    return render(request, 'login.html')


def cria_mensagem(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem_cliente = request.POST.get('mensagem')
        mensagem = Message(nome = nome, email = email, mensagem = mensagem_cliente).save()

        mensage_sucesso = """
            <div class="bg-green-100 border-l-4 border-green-500 text-green-700 p-4 rounded shadow-md">
                <p class="font-bold">Sucesso!</p>
                <p>Sua mensagem foi enviada. Entraremos em contato em breve.</p>
                <a href="" class="text-sm underline mt-2 block">Enviar nova mensagem</a>
            </div>
        """
        return HttpResponse(mensage_sucesso)

    return render(request, 'formulario.html')

@login_required(login_url='/login/')
def lista_mensagens(request):
    mensagens = Message.objects.all().order_by('-id')
    
    data_mensagem = request.GET.get('data')
    texto_mensagem = request.GET.get('texto')
    status_mensagem = request.GET.get('status')
    contato_mensagem = request.GET.get('nome')
    email_mensagem = request.GET.get('email')

    if data_mensagem:
        mensagens = mensagens.filter(data_envio=data_mensagem)
    if texto_mensagem:
        mensagens = mensagens.filter(mensagem__icontains=texto_mensagem)
    if status_mensagem:
        if status_mensagem == 'lida':
            mensagens = mensagens.filter(lido=True)
        elif status_mensagem == 'nao_lida':
            mensagens = mensagens.filter(lido=False)
    if contato_mensagem:
        mensagens = mensagens.filter(nome__icontains=contato_mensagem)
    if email_mensagem:
        mensagens = mensagens.filter(email__icontains=email_mensagem)

    context = {'mensagens': mensagens}

    if request.headers.get('HX-Request'):
        return render(request, '_mensagens_partial.html', context)
    
    return render(request, 'listagem_mensagens.html', context)

def apaga_mensagem(request, id):
    mensagem = get_object_or_404(Message, id=id)
    mensagem.delete()
    return HttpResponse("")


def atualiza_status(request, id):
    mensagem = get_object_or_404(Message, id=id) 
    mensagem.lido = not mensagem.lido
    mensagem.save()
    return render(request, '_mensagens_partial.html', {'mensagens': [mensagem]})


def editar_mensagem(request, id):
    mensagem = get_object_or_404(Message, id=id)
    
    
    if request.method == 'POST':
        novo_conteudo = request.POST.get('conteudo_mensagem')
        
        
        if novo_conteudo:
            mensagem.mensagem = novo_conteudo
            mensagem.save()
            
    return render(request, '_mensagens_partial.html', {'mensagens': [mensagem]})