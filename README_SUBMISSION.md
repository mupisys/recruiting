# 🚀 Projeto Recruiting – Desafio Técnico (Lázaro)

Este projeto foi desenvolvido como parte de um desafio técnico, com foco na construção de uma **landing page funcional** de mensagens, **área administrativa protegida** e **uso de tecnologias modernas no frontend**, mantendo boas práticas de desenvolvimento com **Django**.

---

## 🎯 Objetivo do Projeto

* Criar uma **landing page** com formulário de contato funcional 
* Armazenar mensagens enviadas pelos usuários
* Disponibilizar uma **área administrativa protegida** para gerenciamento das mensagens
* Demonstrar atenção a **UI/UX**, usabilidade e organização de código
* Utilizar **HTMX** e **Alpine.js** para interatividade sem JavaScript pesado

---

## 🛠️ Tecnologias Utilizadas

### Backend

* **Python**
* **Django**
* **SQLite** (banco padrão para desenvolvimento)

### Frontend

* **HTML + Tailwind CSS**
* **HTMX** (envio de formulário sem reload)
* **Alpine.js** (interações simples e modais)
* **UI baseada em componentes reutilizáveis**

---

## ✨ Funcionalidades Implementadas

### Landing Page

* Formulário de contato com:

  * Nome
  * Email
  * Mensagem
* Feedback visual após envio da mensagem
* Design responsivo e focado em usabilidade

### Área Administrativa (Protegida)

* Login customizado
* Listagem de mensagens recebidas
* Visualização individual da mensagem
* Marcação automática como **lida**
* Edição de mensagem
* Exclusão de mensagem com confirmação
* Logout com **confirmação usando Alpine.js**

---

## 🔐 Autenticação

* Área administrativa protegida com `login_required`
* Apenas usuários autenticados podem acessar:
  * Listagem
  * Detalhe
  * Edição
  * Exclusão
* Caso um usuário tente acessar a área administrativa ele será redirecionafo para o login **(por questão de segurança)**

---

## ⚡ Interatividade

### HTMX

* Envio do formulário sem recarregar a página

### Alpine.js

* Modal de confirmação de logout


---

## 📁 Estrutura do Projeto (Simplificada)

```
recruiting/
│
├── app_principal/
│   ├── templates/
|   |   ├── base.html
│   │   ├── landpage.html
│   │   ├── login.html
|   |   ├── logout_confirm.html
|   |   ├── message_delete_confirm.html
|   |   ├── message_detail.html
│   │   ├── message_edit.html
│   │   ├── messages_list.html
│   │   └── partials/
│   |       ├── message_status.html
│   │       └── success.html
│   ├── views.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── static/
│   └── css/
|       ├── output.css
│       └── tailwind.css
│   └── js/
│       └── main.js
│
├── core/
│   ├── settings.py
│   └── urls.py
|
└── README.md
└── README_SUBIMISSION.md
```

---

## ▶️ Como Rodar o Projeto Localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/Lazaro9850/recruiting.git

cd recruiting
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Criar e ativar o ambiente virtual

```bash
python -m venv venv #isso cria o ambiente

#esses dois ativam o ambiente
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 4. Rodar migrações

```bash
python manage.py migrate
```

### 5. Criar superusuário ou usar um existente

```bash
python manage.py createsuperuser

#SUPER USUÁRIO EXISTENTE:
# |User: Lazaro
# |Password: 98504294
```

### 6. Iniciar o servidor

```bash
python manage.py runserver
```

Acesse:

* Landing page: `http://127.0.0.1:8000/`
* Área admin: `http://127.0.0.1:8000/login/`
* Área admin (caso ja tenha logado): `http://127.0.0.1:8000/mensagens/`


---

Desenvolvido por **Lázaro Gabriel Vieira Cardoso**
💻 Estudante de Desenvolvimento de Sistemas | Sempre em busca de soluções práticas, com foco na usabilidade e performance
