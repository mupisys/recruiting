from django.urls import path
from . import views

urlpatterns = [
    path('', views.cria_mensagem, name="enviar_mensagem"),
    path('login/', views.valida_login_adm, name="valida_login"),
    path('lista_mensgens/', views.lista_mensagens, name="lista_mensagens"),
    path('atualiza_status/<int:id>', views.atualiza_status, name="atualiza_status"),
    path('apaga_mensagem/<int:id>', views.apaga_mensagem, name="apaga_mensagem"),
    path('editar/<int:id>/', views.editar_mensagem, name='editar_mensagem')
]
