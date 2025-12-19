from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)
    is_active = models.BooleanField(_("Ativo"), default=True)

    class Meta:
        abstract = True


class Mensagem(models.Model):
    nome = models.CharField(_("Nome"), max_length=120)
    email = models.EmailField(_("Email"))
    mensagem = models.TextField(_("Mensagem"))
    data_envio = models.DateTimeField(_("Enviado em"), auto_now_add=True)
    lido = models.BooleanField(_("Lido"), default=False)

    class Meta:
        verbose_name = _("Mensagem")
        verbose_name_plural = _("Mensagens")

        ordering = ["-data_envio"]

    def __str__(self):
        return f"{self.nome} <{self.email}>"

    def get_absolute_url(self):
        return reverse("message_detail", kwargs={"pk": self.pk})


class ServiceCategory(BaseModel):
    name = models.CharField(_("Nome"), max_length=80)
    slug = models.SlugField(_("Slug"), unique=True, blank=True)
    order = models.PositiveIntegerField(_("Ordem"), default=0)

    class Meta:
        verbose_name = _("Categoria de serviço")
        verbose_name_plural = _("Categorias de serviço")
        ordering = ["order", "name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Service(BaseModel):
    class Icon(models.TextChoices):
        HAND = "hand", _("Hand")
        BABY = "baby", _("Baby")
        HEART = "heart", _("Heart")
        MOON = "moon", _("Moon")
        BRAIN = "brain", _("Brain")
        STETHOSCOPE = "stethoscope", _("Stethoscope")
        BONE = "bone", _("Bone")
        MIC = "mic", _("Mic")
        USERS = "users", _("Users")
        ZAP = "zap", _("Zap")
        APPLE = "apple", _("Apple")
        ACTIVITY = "activity", _("Activity")

    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.PROTECT,
        related_name="services",
        verbose_name=_("Categoria"),
    )
    title = models.CharField(_("Título"), max_length=120)
    description = models.TextField(_("Descrição"))
    icon = models.CharField(_("Ícone"), max_length=20, choices=Icon.choices, default=Icon.STETHOSCOPE)
    order = models.PositiveIntegerField(_("Ordem"), default=0)

    class Meta:
        verbose_name = _("Serviço")
        verbose_name_plural = _("Serviços")
        ordering = ["order", "title"]

    def __str__(self):
        return self.title
