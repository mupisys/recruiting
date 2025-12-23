from django.contrib import admin
from django.urls import path, include

# caminho url para direcionar para o app ou para area do admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_principal.urls')),
]
