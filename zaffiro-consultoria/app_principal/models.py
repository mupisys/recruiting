from django.db import models

class MensagemContato(models.Model):

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    empresa = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False) # Indicador visual necessário

    def __clicada__(self):
        return "Lida" if self.lida else "Não Lida"
    
