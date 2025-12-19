# TechSolutions - Sistema de Gerenciamento de Mensagens

> Projeto desenvolvido como teste técnico para a posição de Desenvolvedor Jr. Full Stack da empresa MuPi Sistemas

## Descrição do Projeto

Sistema completo de gerenciamento de mensagens desenvolvido com Django, incluindo:

- **Landing page moderna** com formulário de contato funcional
- **Área administrativa protegida** para gerenciamento de mensagens
- **CRUD completo** de mensagens
- **Interatividade moderna** com HTMX e Alpine.js
- **Design responsivo** com TailwindCSS

## Tecnologias Utilizadas

### Backend
- **Django 4.2+** - Framework web Python
- **SQLite** - Banco de dados (desenvolvimento)
- **Django Forms** - Validação e processamento de formulários
- **Django Auth** - Sistema de autenticação nativo

### Frontend
- **TailwindCSS** - Framework CSS utilitário (via CDN)
- **HTMX 1.9.10** - Interações assíncronas sem JavaScript complexo
- **Alpine.js 3.x** - Framework JavaScript minimalista para interatividade
- **Google Fonts (Inter)** - Tipografia personalizada

## Estrutura e arquitetura de pastas do Projeto

```
testeMuPi/
├── README.md
├── requirements.txt
├── manage.py
├── core/                   # Configurações principais
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app_principal/          # App principal
│   ├── models.py           # Model Message
│   ├── views.py            # Views da aplicação
│   ├── forms.py            # Formulários Django
│   ├── urls.py             # Rotas do app
│   └── templates/
│       ├── base.html       # Template base
│       ├── base_admin.html # Template base admin
│       ├── landpage.html   # Página inicial
│       ├── login.html      # Tela de login
│       ├── logout_confirm.html
│       ├── messages_list.html
│       ├── message_detail.html
│       ├── message_edit.html
│       ├── message_delete_confirm.html
│       └── partials/       # Fragmentos HTMX
│           ├── message_status.html
│           └── message_status_button.html
├── static/                 # Arquivos estáticos
│   ├── css/
│   ├── js/
│   └── images/
└── media/                  # Uploads de arquivos
```

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python, similar ao npm do JavaScript)

### Passo a Passo

#### Clone o repositório

```bash
git clone <url-do-repositorio>
cd testeMuPi
```

#### Crie e ative um ambiente virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Instale as dependências

```bash
pip install -r requirements.txt
```

#### Configure o banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

#### Crie um superusuário

```bash
python manage.py createsuperuser
```

Siga as instruções para criar um usuário administrador (você precisará dele para acessar a área administrativa).

#### Execute o servidor de desenvolvimento

```bash
python manage.py runserver
```

#### Acesse a aplicação

| Página | URL |
|--------|-----|
| **Landpage** | http://localhost:8000 |
| **Área Admin** | http://localhost:8000/admin |

---
## 📝 Notas Importantes

| Aspecto | Observação |
|-----------|--------------|
| **Liberdade Criativa** | Você tem total liberdade para escolher o tema da landpage |
| **Exemplos** | Consulte a pasta `/examples` para inspiração em design |
| **Foco** | Apesar de ser full stack, **valorizamos muito** as habilidades de UI/UX |
| **Performance** | Considere a experiência do usuário final |
| **Acessibilidade** | Boas práticas de acessibilidade são um **diferencial** |

---

## 💭 Não Conseguiu Completar Tudo?

> **Sem problemas!** Apesar da listagem de requisitos mínimos acima, caso não tenha tido tempo suficiente ou tenha se esbarrado em alguma dificuldade, **entregue o desafio ainda que incompleto** e conte-nos na descrição do Pull Request quais foram as suas maiores dificuldades.

**Não se preocupe, avaliaremos ainda assim!** 😊

O importante é ver seu raciocínio, sua abordagem aos problemas e a qualidade do que você conseguiu desenvolver.

---

## 🤖 Sobre o Uso de Agentes de IA

O uso de **ferramentas de IA** (como ChatGPT, GitHub Copilot, Claude, etc.) **não é proibido**. Na verdade, reconhecemos que essas ferramentas fazem parte do dia a dia do desenvolvimento moderno.

### ⚠️ Importante

**Você DEVE ser capaz de:**

- 📖 **Explicar tecnicamente** cada parte do código que você entrega
- 🧠 **Entender completamente** o que está acontecendo em todas as linhas
- 🔧 **Justificar decisões** de arquitetura e escolhas técnicas
- 🐛 **Debugar problemas** que possam surgir no código
- 💬 **Responder perguntas** sobre qualquer aspecto da implementação

### 🎯 Durante a Avaliação

Na reunião de avaliação, poderemos:
- Pedir explicações sobre trechos específicos do código
- Questionar sobre alternativas às soluções implementadas
- Discutir trade-offs e decisões técnicas tomadas

### 💡 Dica

Use IA como **ferramenta de apoio** e **aceleração**, não como substituto do seu conhecimento. O código gerado por IA deve ser revisado, compreendido e adaptado por você.

**Lembre-se:** O objetivo é avaliar **suas** habilidades técnicas e de raciocínio! 🚀

---

<div align="center">

### Boa sorte com o teste técnico! 🌟

**Mostre suas habilidades e criatividade!**

</div>

