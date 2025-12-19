from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .forms import ContatoForm 
from .models import MensagemContato

# --- PÚBLICO: LANDPAGE ---
def landpage(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            # Retorna o partial para o HTMX
            return render(request, 'partials/success_message.html')
    else:
        form = ContatoForm()
    return render(request, 'landpage.html', {'form': form})

# --- AUTENTICAÇÃO ---
def login_view(request):
    if request.user.is_authenticated:
        return redirect('messages_list')
    
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('messages_list')
    return render(request, 'login.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return render(request, 'logout_confirm.html')

# --- ÁREA ADMINISTRATIVA (DASHBOARD) ---

class MessageListView(LoginRequiredMixin, ListView):
    model = MensagemContato
    template_name = 'messages_list.html'
    context_object_name = 'mensagens'
    login_url = 'login'

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = MensagemContato
    template_name = 'message_detail.html'
    # O Django usa 'object' no template por padrão

class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = MensagemContato
    # Adicionados os campos empresa e telefone que você criou no banco
    fields = ['nome', 'empresa', 'email', 'telefone', 'mensagem', 'lida']
    template_name = 'message_edit.html'
    success_url = reverse_lazy('messages_list')

class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = MensagemContato
    template_name = 'message_delete_confirm.html'
    success_url = reverse_lazy('messages_list')