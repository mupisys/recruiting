from django.urls import path
from .views import landpage

urlpatterns = [
    path("", landpage, name="landpage"),
]
