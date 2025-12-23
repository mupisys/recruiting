from django.urls import path
from . import views

''' 
caminhos url para identificar views
algumas funçoes sao referenciadas por identação
'''
urlpatterns = [
    path('', views.landpage, name='landpage'),
    path('login/', views.login_view, name='login'),
    path('mensagens/', views.messages_list, name='messages_list'),
    path('mensagens/<int:pk>/', views.message_detail, name='message_detail'),
    path('mensagens/<int:pk>/editar/', views.message_edit, name='message_edit'),
    path('mensagens/<int:pk>/deletar/', views.message_delete_confirm, name='message_delete'),
    path('logout/', views.logout_confirm, name='logout'),

]
