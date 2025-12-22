from django import forms
from .models import Mensagem

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ["nome", "email", "mensagem"]
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Seu nome"}),
            "email": forms.EmailInput(attrs={"placeholder": "Seu e-mail"}),
            "mensagem": forms.Textarea(attrs={"placeholder": "Sua mensagem"}),
        }

class MensagemEditForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ["nome", "email", "mensagem"]