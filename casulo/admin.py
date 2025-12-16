from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_envio', 'lido')
    list_filter = ('lido', 'data_envio')
    search_fields = ('nome', 'email', 'mensagem')
    ordering = ('-data_envio',)