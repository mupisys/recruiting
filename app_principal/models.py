from django.db import models

class Message(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    mensagem = models.TextField()
    lido = models.BooleanField(default=False)
    data_envio = models.DateField(auto_now_add=True)

def _str_(self):
    return f"{self.nome} - {self.email}"