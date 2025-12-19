from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q # Importado para permitir buscas complexas
from .forms import ContatoForm 
from .models import MensagemContato

# --- PÚBLICO: LANDPAGE ---
def landpage(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
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
    return render(request, 'admin/login.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return render(request, 'admin/logout_confirm.html')

# --- ÁREA ADMINISTRATIVA (DASHBOARD) ---

class MessageListView(LoginRequiredMixin, ListView):
    model = MensagemContato
    template_name = 'admin/messages_list.html'
    context_object_name = 'mensagens'
    login_url = 'login'
    ordering = ['-id']

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # 1. Filtro por Status (Nova / Lida)
        status_filter = self.request.GET.get('status')
        if status_filter == 'nova':
            queryset = queryset.filter(lida=False)
        elif status_filter == 'lida':
            queryset = queryset.filter(lida=True)

        # 2. Barra de Busca (Filtra por Nome, Empresa ou E-mail)
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(nome__icontains=search_query) | 
                Q(empresa__icontains=search_query) |
                Q(email__icontains=search_query)
            )
            
        return queryset

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = MensagemContato
    template_name = 'admin/message_detail.html'
    context_object_name = 'mensagem'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.lida:
            obj.lida = True
            obj.save()
        return obj

@login_required
def marcar_lida(request, pk):
    mensagem = get_object_or_404(MensagemContato, pk=pk)
    mensagem.lida = not mensagem.lida
    mensagem.save()
    return redirect('messages_list')

class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = MensagemContato
    fields = ['nome', 'empresa', 'email', 'telefone', 'mensagem', 'lida']
    template_name = 'admin/message_edit.html'
    success_url = reverse_lazy('messages_list')

class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = MensagemContato
    template_name = 'admin/message_delete_confirm.html'
    success_url = reverse_lazy('messages_list')