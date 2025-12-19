# HDC Host - Landing Page e Sistema de Mensagens

Esse projeto é uma aplicação web full-stack desenvolvida com Django. A ideia principal é simular o site de uma empresa de hospedagem (HDC Host), contendo uma landing page para apresentação dos serviços e um painel administrativo interno para gerenciar os contatos recebidos.

O foco foi criar uma interface agradável e responsiva, mantendo o backend robusto e simples de manter.

## 🛠 Tecnologias

Nada de complicar o que pode ser simples. A stack escolhida foi:

*   **Django**: Cuida de todo o backend, rotas, ORM e autenticação.
*   **Tailwind CSS**: Para estilização rápida e responsiva (usado via CDN).
*   **Alpine.js**: Para gerenciar estados simples no frontend, como abrir e fechar modais de confirmação.
*   **HTMX**: Para interações dinâmicas sem precisar recarregar a página (ex: marcar mensagem como lida).
*   **PostgreSQL**: Banco de dados relacional robusto (rodando via Docker).
*   **Docker**: Para containerização do banco de dados.

## 🚀 Funcionalidades

### Área Pública
*   **Landing Page**: Seções de Home, Preços e Contato.
*   **Formulário de Contato**: Envio de mensagens com validação e feedback visual (modais de sucesso/erro).

### Área Administrativa (Restrita)
*   **Autenticação**: Sistema de Login, Logout e Cadastro de novos administradores.
*   **Dashboard de Mensagens**: Lista todas as mensagens recebidas pelo site.
*   **Gestão de Leads**:
    *   Visualizar detalhes da mensagem.
    *   Alternar status de leitura (Lido/Não lido) dinamicamente.
    *   Editar informações do contato.
    *   Excluir mensagens (com modal de confirmação para evitar acidentes).

## 🏃‍♂️ Como rodar o projeto

O projeto utiliza Docker para o banco de dados, então certifique-se de ter o Docker e o Docker Compose instalados.

1.  **Clone o repositório e entre na pasta:**
    ```bash
    git clone <seu-repo>
    cd recruiting
    cd src
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Suba o banco de dados e configure o ambiente:**
    ```bash
    # Inicia o PostgreSQL
    docker-compose up -d
    
    # Cria o banco de dados (se não existir)
    python create_database.py
    
    # Aplica as migrações e roda o servidor
    python manage.py migrate
    python manage.py runserver
    ```

Agora é só acessar `http://127.0.0.1:8000`. Para acessar o painel, vá em "Entrar" e crie uma conta na opção de cadastro.