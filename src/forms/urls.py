from django.contrib import admin
from django.urls import path, include
from . import views 

app_name = 'forms'

urlpatterns = [
    path('', views.landpage_view, name="landpage"),
    path('admin/', views.messages_list_view, name="mensagens"),
    path('mensagem/<int:id>/', views.message_detail_view, name="detalhe"),
    path('mensagem/<int:id>/delete/', views.message_delete_view, name="deletar"),
    path('mensagem/<int:id>/edit/', views.message_edit_view, name="editar"),
    path('mensagem/<int:id>/toggle-read/', views.toggle_read_view, name="toggle_read"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
]