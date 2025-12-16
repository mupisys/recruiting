from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
  created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
  updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)
  is_active = models.BooleanField(_("Ativo"), default=True)

  class Meta:
    abstract = True

class Message(models.Model):
    nome = models.CharField(_("Nome"), max_length=120)
    email = models.EmailField(_("Email"))
    mensagem  = models.TextField(_("Mensagem"))
    data_envio = models.DateTimeField(_("Enviado em"), auto_now_add=True)
    lido = models.BooleanField(_("Lido"), default=False)
    

    class Meta:
        verbose_name = _("Messagem")
        verbose_name_plural = _("Messagens")
        
        ordering = ["-data_envio"]

    def __str__(self):
        return f"{self.nome} <{self.email}>"

    def get_absolute_url(self):
        return reverse("message_detail", kwargs={"pk": self.pk})
