<img src="static/images/LogoDinamico.gif" alt="Casulo" width="180"/>

# Casulo — Landing Page + Painel de Mensagens (Django + Tailwind + HTMX + Alpine)

Projeto desenvolvido para o teste técnico da **Mupi Systems**: uma **landpage moderna e responsiva** com formulário de contato funcional e uma **área administrativa protegida** para gerenciamento das mensagens recebidas.

---

## ✨ Visão geral

**Casulo** é uma clínica multidisciplinar com uma experiência visual “clean”, prestando serviços para o corpo e mente, seu site possui um formulário de contato funcional e uma área administrativa protegida para gerenciamento das mensagens recebidas.

- Visitante acessa o site → envia mensagem pelo formulário
- Admin acessa o painel → filtra/busca mensagens → visualiza, edita, exclui e marca como lida/não lida

---

## ✅ Funcionalidades implementadas

### 🌐 Área pública (Landpage)
- **Seções completas** (sobre, serviços, equipe, espaço, depoimentos, contato)
- **Formulário de contato funcional** com validação (Django Forms)
- Envio do formulário com **HTMX** (sem reload, re-render do formulário via partial)
- **Serviços com categorias** + filtro dinâmico com **HTMX** (`/partials/services/`)
- **Galeria do espaço** carregada automaticamente lendo `static/images/espaco/`
- Navbar responsiva com **Alpine.js** (menu mobile, efeito “scrolled”)

### 🔐 Painel administrativo (protegido)
Rotas sob `/painel/` com autenticação (Django Auth):

- **Pagina de Login personalizada**
- **Listagem de mensagens** com:
  - filtro por status (lida/não lida)
  - busca por nome ou email
  - filtro por data
  - atualização de resultados via **HTMX**
- **Detalhe da mensagem**
- **Edição da mensagem**
- **Exclusão com confirmação** via modal (Alpine)
- **Marcar como lida/não lida** via **HTMX**
  - comportamento inteligente: se a mensagem “sai” do filtro atual, o item é removido da tela sem recarregar

### 🎨 UX/UI extras
- **Tema claro/escuro** (toggle flutuante)
- **Lucide Icons** via CDN
- Modal genérico de confirmação (Alpine)
---

## 🧰 Stack / Tecnologias
- **Django 6**
- **Django Templates**
- **TailwindCSS v4 (CLI)**
- **HTMX**
- **Alpine.js**

---

## 🚀 Como rodar o projeto (passo a passo)

### Pré-requisitos
- **Python 3.10+**
- **Node.js 18+** (para o Tailwind CLI)

### 1) Clone e entre na pasta
```bash
git clone https://github.com/GahCunha/recruiting_mupi.git
cd recruiting_mupi
```

### 2) Crie e ative a venv
**Windows (PowerShell):**
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Instale as dependências Python
```bash
pip install -r requirements.txt
```

### 4) Migre o banco
```bash
python manage.py migrate
```

### 5) Crie um superusuário (para acessar o painel)
```bash
python manage.py createsuperuser
```

### 6) Carregar dados iniciais de Serviços/Categorias
```bash
python manage.py loaddata casulo/fixtures/initial_services.json casulo/fixtures/team_members.json
```

### 7) Rode o servidor
```bash
python manage.py runserver
```

---

## 🎨 TailwindCSS

O CSS estará em `static/css/output.css`. basta rodar `npm run tw:build` para compilar.

```bash
npm run tw:build
```
caso queira compilar em tempo real, use:
```bash
npm run tw:watch
```

---

## 📍 Rotas principais

| Página | URL |
|------|-----|
| Landpage | `http://127.0.0.1:8000/` |
| Login do Painel | `http://127.0.0.1:8000/painel/login/` |
| Mensagens (Painel) | `http://127.0.0.1:8000/painel/mensagens/` |
| Django Admin (opcional) | `http://127.0.0.1:8000/admin/` |

---

## 🧠 Decisões técnicas

- **HTMX + partials**: usei para manter o Django Templates simples(filtros, submit, toggles).
- **Alpine.js**: preferi para microinterações (menu mobile, modal de confirmação reaproveitável).
- **Serviços em modelos próprios + fixture**: dá controle editorial (categoria, ordem, ativo) sem hardcode no template.
- **Galeria lendo arquivos do diretório**: diminui trabalho manual para atualizar a seção “Espaço”.

---

## 📁 Estrutura do projeto (resumo)

```text
recruiting_mupi/
├── core/                  # settings/urls do Django
├── casulo/                # app principal
│   ├── models.py          # Mensagem, ServiceCategory, Service
│   ├── views.py           # landpage + painel + HTMX endpoints
│   ├── fixtures/          # initial_services.json
│   └── templates/         # base, landpage, login, painel + partials
├── static/
│   ├── css/               # input.css / output.css
│   ├── js/                # theme, ui, csrf htmx, carousel
│   └── images/            # assets + espaco/
├── manage.py
├── requirements.txt
├── package.json           # Tailwind CLI scripts
```