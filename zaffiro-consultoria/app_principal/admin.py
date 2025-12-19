from django.contrib import admin
from .models import MensagemContato

@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_envio', 'lido')
    list_filter = ('lido', 'data_envio')