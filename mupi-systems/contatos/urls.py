from django.urls import path
from . import views

urlpatterns = [
    path('', views.landpage, name='landpage'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_confirm, name='logout_confirm'),

    # Mensagens
    path('admin/messages/', views.messages_list, name='messages_list'),
    path('admin/messages/<int:pk>/', views.message_detail, name='message_detail'),
    path('admin/messages/<int:pk>/edit/', views.message_edit, name='message_edit'),
    path('admin/messages/<int:pk>/delete/', views.message_delete, name='message_delete'),
    path('admin/messages/<int:pk>/toggle/', views.message_toggle_read, name='message_toggle_read'),
    path('admin/messages/contadores/', views.contadores, name='contadores'),




    # HTMX - Adicionar esta linha
    path('admin/messages/<int:pk>/marcar-lida/', views.marcar_lida, name='marcar_lida'),

    # HTMX - Adicionar esta linha
    path('admin/messages/contadores/', views.contadores, name='contadores'),

]
