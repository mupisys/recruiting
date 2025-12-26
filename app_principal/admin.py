from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'mensagem', 'lido', 'data_envio')
    search_fields = ('nome', 'email', 'mensagem', 'lido', 'data_envio')

