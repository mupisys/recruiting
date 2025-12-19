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
├── core/                                                # Configurações principais
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app_principal/                                       # App principal
│   ├── models.py                                        # Model Message
│   ├── views.py                                         # Views da aplicação
│   ├── forms.py                                         # Formulários Django
│   ├── urls.py                                          # Rotas do app
│   └── templates/
│       ├── base.html                                    # Template base
│       ├── base_admin.html                              # Template base admin
│       ├── landpage.html                                # Página inicial
│       ├── login.html                                   # Tela de login
│       ├── logout_confirm.html
│       ├── messages_list.html
│       ├── message_detail.html
│       ├── message_edit.html
│       ├── message_delete_confirm.html
│       └── partials/                                    # Fragmentos HTMX
│           ├── message_status.html
│           └── message_status_button.html
├── static/                                              # Arquivos estáticos
│   ├── css/
│   ├── js/
│   └── images/
└── media/                                               # Uploads de arquivos
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

| Página                 |   URL                              |
|------------------------|------------------------------------|
| **Landpage**           |   http://localhost:8000            |
| **Área Admin**         |   http://localhost:8000/admin      |
| **Lista de Mensagens** |   http://localhost:8000/messages/  |


#### Model de dados
		
|  name      |   CharField(100)    |  Nome do remetente                   |
|------------|---------------------|--------------------------------------|
|  email     |   EmailField        |  Email do remetente                  |  
|  message   |   TextField         |  Conteúdo da mensagem                |
|  createdAt |   DateTimeField     |  Data da criação da mensagem         |
|  isRead    |   BooleanField      |  Status de leitura (default: False)  |

## Rotas da Aplicação

### Públicas
- `/` : Landpage com formulário de contato
- `/login/` : Tela de login

### Protegidas (requer autenticação)
- `/messages/` : Lista todas as mensagens
- `/messages/<id>/` : Detalhes de uma mensagem
- `/messages/<id>/edit/` : Editar mensagem
- `/messages/<id>/delete/` : Confirmar exclusão
- `/messages/<id>/toggle-read/` : Marcar/desmarcar como lida (HTMX)
- `/logout/` : Confirmar logout

### Requisitos Mínimos Atendidos
- Formulário público na landpage salvando mensagens
- Login customizado (não usa admin padrão)
- Área administrativa protegida com `@login_required`
- CRUD completo de mensagens
- Marcar mensagem como lida/não lida com HTMX (sem reload)
- Logout com confirmação
- Design responsivo
- TailwindCSS para todo o layout
- HTMX implementado (marcar como lida)
- Alpine.js implementado (notificações e animações)

### Diferenciais Implementados
- Fontes personalizadas - Google Fonts (Inter)
- Contraste bem trabalhado - Paleta de cores acessível
- Identidade visual consistente - Gradientes e cores harmoniosas
- Animações suaves - Transições e microinterações
- Design mobile-first - Totalmente responsivo
- Indicadores de loading - Feedback visual nas requisições HTMX

## Decisões Técnicas

### Por que Django?
- Framework robusto e maduro para desenvolvimento web
- Sistema de autenticação nativo e seguro
- ORM poderoso para interação com banco de dados
- Templates integrados facilitam desenvolvimento

### Por que HTMX?
- Permite interações assíncronas sem JavaScript complexo
- Ideal para marcar mensagens como lidas sem recarregar a página
- Reduz a complexidade do frontend mantendo o código no servidor

### Por que Alpine.js?
- Framework JavaScript minimalista e leve
- Perfeito para controlar modais e pequenas animações de interface
- Complementa o HTMX sem necessidade de build process

### Por que TailwindCSS?
- Estilização rápida e consistente com classes utilitárias
- Design responsivo facilitado
- Manutenção simplificada do layout

### Segurança
- Proteção CSRF em todos os formulários
- Autenticação obrigatória para área administrativa
- Validação de formulários no backend
- Sanitização de dados de entrada

## Próximos Passos (Melhorias Futuras)
- Adicionar filtros de busca na listagem
- Implementar paginação para grandes volumes de dados
- Adicionar exportação de mensagens (CSV/PDF)
- Sistema de notificações por email
- Suporte a múltiplos idiomas (i18n)

## Licença
Este projeto foi desenvolvido para fins de avaliação técnica.

**Nota:** Este é um projeto de teste técnico. Para uso em produção, considere trocar o SQLite por PostgreSQL e configurar variáveis de ambiente para dados sensíveis.
