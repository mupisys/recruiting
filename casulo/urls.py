from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.landpage, name="landpage"),
    
     # painel (auth)
    path("painel/login/", auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name="login"),
    path("painel/logout/", views.logout_confirm, name="logout_confirm"),

    path("painel/mensagens/", views.messages_list, name="messages_list"),
    path("painel/mensagens/<int:pk>/", views.message_detail, name="message_detail"),
    path("painel/mensagens/<int:pk>/editar/", views.message_edit, name="message_edit"),
    path("painel/mensagens/<int:pk>/toggle-read/", views.message_toggle_read, name="message_toggle_read"),
    path("painel/mensagens/<int:pk>/excluir/", views.message_delete_confirm, name="message_delete_confirm"),
    
    path("partials/services/", views.services_partial, name="services_partial"),
]
