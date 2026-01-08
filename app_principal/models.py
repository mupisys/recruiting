from django.db import models

class Message(models.Model):

    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Mensagem')
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    isRead = models.BooleanField(default=False, verbose_name='Lida')

    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'
        ordering = ['-createdAt']

    def __str__(self):
        return f"{self.name} - {self.email}"