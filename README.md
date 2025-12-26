Projeto Django — Teste Técnico Mupisys
Este projeto foi desenvolvido como parte de um teste técnico para a empresa Mupisys. A aplicação foi construída utilizando o framework Django e tem como objetivo demonstrar conhecimentos em autenticação, persistência de dados, organização de views e templates, e implementação completa de operações CRUD.

🚀 Tecnologias Utilizadas

Python

Django

Django ORM

HTML + Templates do Django

Tailwind / CSS via CDN (ou o que você usou)

SQLite (ou substitua pelo seu banco)

Funcionalidades Implementadas
✔ Autenticação de usuários

Implementada utilizando os módulos nativos do Django

Login, logout e controle de sessão

Proteção de rotas com o decorator @login_required

✔ Organização do Projeto

Views separadas por responsabilidade

Templates estruturados e integrados ao Django

Boas práticas de arquitetura

✔ CRUD Completo de Mensagens

Criação de mensagens

Listagem de mensagens

Visualização de detalhes

Edição

Exclusão

✔ Persistência de Dados

Utilização do Django ORM

Consultas estruturadas em models

Relacionamento com usuários (se aplicável)

✔ Interface

Templates renderizados dinamicamente

Estilização via CDN

Como Executar o Projeto
Clone o repositório (git@github.com:JoandersonOliveira/recruiting.git) (https://github.com/JoandersonOliveira/recruiting.git)

Crie e ative um ambiente virtual
python -m venv venv venv\Scripts\activate - Windows

source venv/bin/activate - Linux/Mac

Instale as dependências
pip install -r requirements.txt

execute as migrações
python manage.py migrate

Crie um superusuario
python manage.py createsuperuser

Inicie o servidor
python manage.py runserver

Acesse em: 👉 http://127.0.0.1:8000/ 👉 http://127.0.0.1:8000/login/
