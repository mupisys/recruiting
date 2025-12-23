from django.contrib import admin
from .models import Mensagem

#model registrada ao admin
@admin.register(Mensagem) # pode ser acessada no painel admin do Django
class MensagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_envio', 'lido') # cria campos em forma de tabela
    list_filter = ('lido', 'data_envio') # cria filtos nas colunas
    search_fields = ('nome', 'email', 'mensagem') # cria barra de busca
