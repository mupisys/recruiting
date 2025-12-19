from django import forms
from .models import MensagemContato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = MensagemContato
        fields = ['nome', 'email', 'telefone', 'mensagem']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        estilo = "w-full p-4 bg-gray-50 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-600 outline-none transition-all"
        
        self.fields['nome'].widget.attrs.update({'class': estilo, 'placeholder': 'Seu nome completo'})
        self.fields['email'].widget.attrs.update({'class': estilo, 'placeholder': 'Seu melhor e-mail'})
        
        self.fields['telefone'].widget.attrs.update({'class': estilo, 'placeholder': '(00) 00000-0000'})
        
        self.fields['mensagem'].widget.attrs.update({'class': estilo, 'placeholder': 'Como podemos ajudar?', 'rows': '4'})