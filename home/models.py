from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mensagem = models.TextField(max_length=500)

class Administrador(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    criado_em = models.DateTimeField(auto_now_add=True)