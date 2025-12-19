from django.contrib import admin
from django.urls import path, include
from . import views 

app_name = 'forms'

urlpatterns = [
    path('', views.createMessageView, name="Home"),
    path('admin/', views.getAllMessagesView, name="mensagens"),
    path('delete/<int:id>', views.deleteMessageByIdView, name="deletar"),
    path('edit/<int:id>', views.editMessageByIdView, name="editar"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
]