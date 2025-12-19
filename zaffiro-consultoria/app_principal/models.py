from django.db import models

class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    # Permitir que empresa e telefone fiquem vazios no banco se o usuário não preencher
    empresa = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    
    lida = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} - {self.email}"

    def status_leitura(self):
        return "Lida" if self.lida else "Não Lida"