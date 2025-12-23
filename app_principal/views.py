# imports para funcao landpage
from django.shortcuts import render
from .models import Mensagem

# imports para funcao login_view
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# import para funcoes e paginas da area do admin
from django.contrib.auth.decorators import login_required

# import para o uso de operaçoes com o DB
from django.shortcuts import get_object_or_404

# import para a funcao logout_confirm
from django.contrib.auth import logout

#ja salva no banco
def landpage(request):
    
    # confirma o metodo post
    if request.method == "POST":
        # a model Mensagens recebe seus dados
        Mensagem.objects.create(
            nome=request.POST.get("nome"),
            email=request.POST.get("email"),
            mensagem=request.POST.get("mensagem"),
        )
        return render(request, "partials/success.html") # retorna mensagem de sucesso

    return render(request, "landpage.html") # se nao for pelo metodo post, fica na pagina ainda

def login_view(request):
    # confirma o metodo post e tenta autentificar
    if request.method == "POST":
        # coleta as informações de login
        username = request.POST.get("username")
        password = request.POST.get("password")

        # essa funçao authenticate confirma se tem algum usuario q tenha esse username e essa senha
        # caso tenha ela retorna um objeto User, caso contrario retorna none
        user = authenticate(request, username=username, password=password)

        # verifica se a variavel user nao é "none"
        if user:
            # cria na secao do admin (entra na secao)
            login(request, user)
            # mostra as mensagens
            return redirect("messages_list")
    
    # se nao for post permanece na pagina de login
    return render(request, "login.html")

# apenas o admin logado consegue visualizar
@login_required
def messages_list(request): # requisicao
    # busca todos registros na model Mensagens
    mensagens = Mensagem.objects.all().order_by('-data_envio') # ordena do mais recente ao mais antigo
    # retorna um dicionario para apresenta-lo no html
    return render(request, 'messages_list.html', {'mensagens': mensagens})

# apenas o admin logado consegue visualizar
@login_required
def message_detail(request, pk): # pk é a primary key da msg que quero ver 
    # busca no banco um objeto da model Mensagem e caso nao tenha retorne 404
    mensagem = get_object_or_404(Mensagem, pk=pk)

    # verifica se a mensagem foi lida (execulta quando ela nao foi lida ainda)
    if not mensagem.lido:
        # altera a mensagem para lida e salva
        mensagem.lido = True
        mensagem.save()

    # redireciona o html e mostra a mensagem que foi recebida na linha 66
    return render(request, "message_detail.html", {"mensagem": mensagem})

# apenas o admin logado consegue visualizar
@login_required
def message_edit(request, pk):
    mensagem = get_object_or_404(Mensagem, pk=pk)
    '''
    essa funcao é basicamente a mesma da landpage (mensagem)
    a diferenca é que usa a primary key para alterar a messagem
    '''
    #verifica se é metodo post para editar a msg se nao for apenas visualisa a msg (get)
    if request.method == "POST":
        mensagem.nome = request.POST.get("nome")
        mensagem.email = request.POST.get("email")
        mensagem.mensagem = request.POST.get("mensagem")
        mensagem.save()

        return redirect("message_detail", pk=mensagem.pk)

    return render(request, "message_edit.html", {"mensagem": mensagem})

# apenas o admin logado consegue visualizar
@login_required
def message_delete_confirm(request, pk):
    # pega o objeto da msg com a primary key 
    mensagem = get_object_or_404(Mensagem, pk=pk)

    if request.method == "POST":
        # deleta a objeto coletado
        mensagem.delete()
        # redireciona para ver a lista completa das msg dnv 
        return redirect("messages_list")

    return render(request, "message_delete_confirm.html", {"mensagem": mensagem})

# apenas o admin logado consegue visualizar
@login_required
def logout_confirm(request):
    if request.method == "POST":
        # essa funçao retira as credenciais do admin
        logout(request)
        # volta para pag de login para logar novamente caso queira
        return redirect("login")
    # confirmação visual logout (apenas exibe a pagina de confirmacao)
    return render(request, "logout_confirm.html")

