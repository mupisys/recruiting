from django.urls import path
from . import views

app_name = 'app_principal'

urlpatterns = [
    path('', views.landpage, name='landpage'),
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('messages/', views.messages_list, name='messages_list'),
    path('messages/<int:message_id>/', views.message_detail, name='message_detail'),
    path('messages/<int:message_id>/edit/', views.message_edit, name='message_edit'),
    path('messages/<int:message_id>/delete/', views.message_delete, name='message_delete'),
    path('messages/<int:message_id>/toggle-read/', views.toggle_read, name='toggle_read'),
]