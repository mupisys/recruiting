from django import forms
from .models import Mensagem


class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['nome', 'email', 'mensagem', 'lido']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'mt-1 block w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-green-500 focus:border-green-500 transition duration-150',
                'placeholder': 'Seu nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'mt-1 block w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-green-500 focus:border-green-500 transition duration-150',
                'placeholder': 'seu@email.com'
            }),
            'mensagem': forms.Textarea(attrs={
                'class': 'mt-1 block w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-green-500 focus:border-green-500 transition duration-150',
                'rows': 5,
                'placeholder': 'Digite sua mensagem aqui...'
            }),
        }
        labels = {
            'nome': 'Nome Completo',
            'email': 'Email',
            'mensagem': 'Mensagem'
        }