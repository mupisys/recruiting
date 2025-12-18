<<<<<<< HEAD
<img src="logo.png" alt="Mupi Systems Logo" width="200"/>

# 🚀 Teste Técnico - Desenvolvedor Jr. Full Stack

---

## 🎯 Objetivos

- Desenvolver uma **landpage atraente** com formulário de contato funcional
- Criar uma **área administrativa protegida** para gerenciamento de mensagens
- Demonstrar habilidades em **UI/UX design** com foco em estética e usabilidade
- Aplicar boas práticas de desenvolvimento **Django** e **frontend moderno**
- Implementar interatividade usando **HTMX** e **Alpine.js**

---

## 📋 Instruções

### 🔀 Fork do Repositório

1. Faça um **fork** deste repositório para sua conta pessoal do GitHub
2. Trabalhe em seu próprio fork

### 💻 Implementação

- Desenvolva o projeto conforme os requisitos abaixo
- Use **Django**, **Django Templates**, **TailwindCSS**, **HTMX** e **Alpine.js** conforme apropriado

### 📤 Submissão

1. Após finalizar, abra um **Pull Request** do seu fork para o repositório original
2. Aguarde o agendamento da reunião para avaliação do teste

### 📝 Documentação

Inclua um arquivo `README.md` com:
- ✅ Descrição do projeto
- ✅ Passo a passo para rodar a aplicação
- ✅ Decisões técnicas importantes

---

## 🛠️ Requisitos Técnicos Mínimos

### 🐍 Backend (Django)

| Requisito | Descrição |
|-----------|-----------|
| **Versão do Django** | 4.0 ou superior |
| **Templates Obrigatórios** | • `landpage.html` - Página inicial com formulário<br>• `login.html` - Tela de login personalizada<br>• `messages_list.html` - Listagem de mensagens<br>• `message_detail.html` - Visualização individual<br>• `message_edit.html` - Edição de mensagem (ou modal)<br>• `message_delete_confirm.html` - Confirmação de exclusão (ou modal)<br>• `logout_confirm.html` - Confirmação de logout (ou modal) |
| **Model** | Mensagem com campos: `nome`, `email`, `mensagem`, `data_envio`, `lido` (boolean) |
| **Autenticação** | Sistema de autenticação para área administrativa |
| **CRUD de Mensagens** | Admin deve poder visualizar, editar e apagar mensagens |
| **Views e URLs** | Views para processar o formulário e gerenciar mensagens com URLs configuradas |

### 🎨 Frontend

#### Tecnologias Obrigatórias

- **TailwindCSS** - Para estilização (obrigatório)
- **HTMX** - Para interações assíncronas (pelo menos uma implementação)
- **Alpine.js** - Para interatividade (pelo menos uma implementação)

#### Requisitos de Interface

- Design **responsivo**
- Formulário **funcional** na landpage
- Tabela/listagem de mensagens na área admin

### 🧹 Qualidade de Código

- Versionamento com **commits semânticos**
- Estrutura de projeto Django **organizada**
- Código **limpo** e bem documentado
- Arquivos estáticos organizados

---

## 🎨 Critérios de Avaliação

### UI/UX Design
- Estética visual atraente
- Experiência de usuário intuitiva
- Consistência visual
- Responsividade

### Qualidade de Código
- Organização do projeto
- Clareza e legibilidade
- Boas práticas Django
- Separação de responsabilidades

### Funcionalidade
- Todos os requisitos mínimos atendidos
- Funcionamento correto das features
- Tratamento de erros

### Versionamento
- Commits descritivos e organizados
- Estrutura de branches (se aplicável)
- Mensagens de commit claras

### Uso das Tecnologias
- Aplicação apropriada de HTMX e Alpine.js
- Eficiência no uso do Tailwind
- Decisões técnicas justificadas

---

## ✨ Diferenciais

Os seguintes elementos serão considerados **pontos extras** na avaliação:

### Design e UX
- 🎨 **Fontes personalizadas** - Uso de tipografia além das fontes padrão do sistema
- 🌗 **Contraste bem trabalhado** - Bom uso de cores, contraste adequado para acessibilidade
- 🎭 **Identidade visual consistente** - Paleta de cores coesa, elementos visuais harmônicos
- ⚡ **Animações e transições suaves** - Microinterações que melhoram a experiência
- 📱 **Design mobile-first** - Experiência otimizada para dispositivos móveis

### Funcionalidades Avançadas com HTMX e Alpine.js
- 🔔 **Modais para confirmações** - Implementar logout, edição e exclusão de mensagens via modal usando HTMX/Alpine.js
- ✏️ **Edição inline** - Editar mensagens diretamente na listagem sem recarregar a página
- 🗑️ **Exclusão com confirmação dinâmica** - Modal de confirmação antes de apagar, com feedback visual
- 🔄 **Marcar como lida sem reload** - Alternar status de mensagem usando HTMX
- 🔍 **Busca e filtros avançados** - Sistema de busca por texto, filtros por data ou status com HTMX
---

## 💡 Diretrizes Criativas

### 🌐 Landpage

> **Liberdade total!** Escolha qualquer produto/serviço de sua preferência (pode ser real ou fictício)

**Sugestões de temas:**
- 📱 Aplicativo mobile ou SaaS
- 🏋️ Academia ou estúdio fitness
- 🍕 Restaurante ou delivery de comida
- 💼 Agência de marketing digital
- 🏠 Imobiliária ou arquitetura
- 🎓 Plataforma de cursos online
- 👔 Consultoria empresarial
- 🎨 Portfólio criativo ou design studio
- 🚗 Serviços automotivos
- 💻 Empresa de tecnologia/software house

**Exemplos na pasta `/examples`** (boas referências de design)

#### Elementos Essenciais

| Seção | Descrição |
|-------|-----------|
| **Header** | Menu de navegação |
| **Hero Section** | Banner principal chamativo |
| **Features/Benefícios** | Destaques do produto/serviço |
| **Formulário de Contato** | Form funcional e validado |
| **Footer** | Informações de rodapé |

### 🔐 Área Administrativa

#### Funcionamento

A área administrativa é uma **seção protegida** que requer autenticação. O fluxo funciona da seguinte forma:

1. **Criação de Usuário Administrador**
   - Durante a configuração inicial, você deve criar um superusuário usando `python manage.py createsuperuser`
   - Este usuário terá acesso à área administrativa

2. **Sistema de Login**
   - Implemente uma **página de login personalizada** (não usar o admin padrão do Django)
   - Design deve seguir a identidade visual do projeto
   - Apenas usuários autenticados podem acessar a área de visualização de mensagens
   - Use o sistema de autenticação nativo do Django (`django.contrib.auth`)

3. **Proteção de Rotas**
   - Use decorators como `@login_required` para proteger as views administrativas
   - Redirecione usuários não autenticados para a página de login

#### Telas Obrigatórias

| Tela | Descrição |
|------|-----------|
| **Landpage** | Página pública com formulário de contato funcional |
| **Login** | Tela personalizada para autenticação do admin |
| **Listagem de Mensagens** | Exibe todas as mensagens com indicador de lidas/não lidas |
| **Visualização Individual** | Detalhes completos de uma mensagem específica |
| **Edição de Mensagem** | Formulário para editar dados de uma mensagem (ou modal) |
| **Confirmação de Exclusão** | Página de confirmação antes de apagar mensagem (ou modal) |
| **Confirmação de Logout** | Página de confirmação antes de deslogar (ou modal) |

#### Funcionalidades de Gerenciamento

O admin deve ser capaz de:

- ✅ **Visualizar** todas as mensagens em uma lista
- ✅ **Abrir** mensagens individuais para ver detalhes completos
- ✅ **Editar** mensagens (corrigir dados, adicionar notas)
- ✅ **Apagar** mensagens
- ✅ **Marcar como lida/não lida**
- ✅ **Fazer logout** com confirmação

#### Características da Interface

- Design **clean** e funcional
- **Indicador visual** de mensagens lidas/não lidas (ex: badge, cor diferente, ícone)
- **Ações rápidas** na listagem (apagar, marcar como lida)
- **Filtros opcionais**: por status (lida/não lida), por data
- **Responsividade** em todas as telas administrativas

#### Exemplo de Fluxo Completo
```
Visitante → Preenche formulário na landpage → Mensagem salva no banco

Admin → Acessa /login → Preenche credenciais → Redireciona para lista de mensagens

Admin → Visualiza lista → Clica em mensagem → Vê detalhes completos

Admin → Clica em "Editar" → Abre tela/modal de edição → Salva alterações → Retorna

Admin → Clica em "Apagar" → Confirma exclusão → Mensagem deletada → Retorna à lista

Admin → Clica em logout → Confirma logout → Deslogado
```

---

## 📁 Estrutura Esperada

```text
seu-projeto/
├── README.md
├── requirements.txt
├── manage.py
├── core/
│   ├── settings.py
│   └── urls.py
├── app_principal/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── base.html
│       ├── landpage.html
│       ├── login.html
│       ├── logout_confirm.html
│       ├── messages_list.html
│       ├── message_detail.html
│       ├── message_edit.html
│       └── message_delete_confirm.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── media/
└── examples/
    └── (referências visuais)
```

---
## 🚀 Como Rodar a Aplicação (Template para seu README)

> **💡 Dica:** No seu README.md, inclua uma seção similar a esta:

### � Instalação e Execução

#### 1️⃣ Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```

#### 2️⃣ Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

#### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure o banco de dados
```bash
python manage.py migrate
```

#### 5️⃣ Crie um superusuário
```bash
python manage.py createsuperuser
```

#### 6️⃣ Execute o servidor
```bash
python manage.py runserver
```

#### 7️⃣ Acesse a aplicação

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
=======
# Heritage Auto

Sistema voltado para o público entusiasta do mundo automobilístico e motociclismo. A plataforma oferece um espaço para notícias oficiais, feed da comunidade, interações sociais e um sistema de mensagens diretas entre usuários.

## Funcionalidades do Sistema

- **Feed de Notícias e Comunidade**: Visualize notícias oficiais e postagens da comunidade em uma interface moderna.
- **Postagens**: Usuários podem criar postagens com títulos, conteúdo, imagens ou vídeos.
- **Interação Social**: Sistema de curtidas e comentários em postagens.
- **Mensagens (Chat)**: Sistema de mensagens estilo "conversa" entre usuários, com atualizações em tempo real (polling) e suporte a respostas.
- **Busca de Usuários**: Autocomplete para encontrar outros usuários para iniciar conversas.
- **Autenticação**: Cadastro e login de usuários.

## Ferramentas Utilizadas

- **Backend**: Django 5.0, Django REST Framework (DRF).
- **Frontend**: Django Templates, Alpine.js (para interatividade e consumo de API), Tailwind CSS (estilização).
- **Banco de Dados**: SQLite.
- **Outros**: `pillow` (processamento de imagens), `django-filter`.

## Estrutura de Arquivos

O projeto segue a estrutura solicitada com `core` para configurações e `app` para a lógica de negócios. Abaixo estão os caminhos principais:

- **Configurações do Projeto (Core)**: `core/`
- **Lógica da Aplicação**: `app/`
- **Templates HTML**: `app/templates/`
- **Scripts Alpine.js/JS e Tailwind**: `static/` (subpastas: `home/`, `messages/`, `js/`, `posts/`, `layouts`)
- **Fixtures (Dados)**: `app/fixtures/`

## Categorias
- Clássicos
- Harley Davidson
- Formula 1
- Le Mans
- Games e Simuladores
- Novidades do Mercado
- Carros e Motos de Luxo

## Instalação e Inicialização

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute as migrações:**
   ```bash
   python manage.py migrate
   ```

3. **Carregue os dados iniciais (Fixtures):**
   O projeto conta com uma fixture contendo dados de exemplo (categorias, posts, usuários).
   ```bash
   python manage.py loaddata app/fixtures/initial_data.json
   ```

4. **Crie um superusuário (Opcional):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Execute o servidor:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

O sistema utiliza uma API REST para diversas funcionalidades dinâmicas. Abaixo estão os principais endpoints:

### Posts e Interações
- `GET /api/posts/`: Lista postagens (suporta filtro `?is_official=true/false`).
- `GET /api/posts/<id>/`: Detalhes de uma postagem.
- `POST /api/posts/<id>/like/`: Curtir/Descurtir uma postagem.
- `POST /api/posts/<id>/comment/`: Adicionar um comentário.
- `GET /api/categories/`: Lista todas as categorias.

### Mensagens e Usuários
- `GET /api/users/search/?q=<query>`: Busca usuários por nome (autocomplete).
- `GET /api/messages/`: Lista conversas do usuário.
- `POST /api/messages/`: Envia uma nova mensagem.
- `GET /api/messages/conversation/<username>/`: Obtém o histórico de mensagens com um usuário específico.
- `DELETE /api/messages/<id>/`: Apaga uma mensagem (apenas o remetente).
>>>>>>> 1d0fad8 (feat: initialize Django project structure)

