from django.contrib import admin
from .models import MensagemContato

@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'empresa', 'lida', 'data_envio')
    list_filter = ('lida', 'data_envio')
    
    search_fields = ('nome', 'email', 'empresa')