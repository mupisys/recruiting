from django.contrib import admin
from .models import Mensagem

#model registrada ao admin
@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_envio', 'lido')
    list_filter = ('lido', 'data_envio')
    search_fields = ('nome', 'email', 'mensagem')
