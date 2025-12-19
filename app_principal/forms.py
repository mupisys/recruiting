from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    """
    Formulário para criação de mensagens na landpage.
    
    Usa ModelForm para facilitar a validação e criação do objeto Message.
    """
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Seu nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'seu@email.com'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Sua mensagem...',
                'rows': 5
            })
        }
        labels = {
            'name': 'Nome',
            'email': 'Email',
            'message': 'Mensagem'
        }

class MessageEditForm(forms.ModelForm):
    """
    Formulário para edição de mensagens na área administrativa.
    
    Permite editar todos os campos, incluindo o status de leitura.
    """
    class Meta:
        model = Message
        fields = ['name', 'email', 'message', 'isRead']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'rows': 5
            }),
            'isRead': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 text-blue-600 rounded focus:ring-blue-500'
            })
        }
        labels = {
            'name': 'Nome',
            'email': 'Email',
            'message': 'Mensagem',
            'isRead': 'Marcar como lida'
        }