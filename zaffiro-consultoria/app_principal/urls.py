from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Rota da Landpage (Página Inicial)
    path('', views.landpage, name='landpage'),

    # Autenticação
    path('login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='admin/logout_confirm.html'), name='logout'),

    # Dashboard de Mensagens (Área Administrativa)
    path('dashboard/', views.MessageListView.as_view(), name='messages_list'),
    path('mensagem/<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
    path('mensagem/<int:pk>/editar/', views.MessageUpdateView.as_view(), name='message_edit'),
    path('mensagem/<int:pk>/deletar/', views.MessageDeleteView.as_view(), name='message_delete'),
    
    # Rota para marcar como lida
    path('mensagem/<int:pk>/marcar-lida/', views.marcar_lida, name='marcar_lida'),
]