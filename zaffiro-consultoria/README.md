# Zaffiro Consultoria - Gestão de Leads

Este projeto é uma aplicação web desenvolvida em **Django** para a Zaffiro Consultoria. Ele consiste em uma Landpage institucional com um formulário de captura de leads e um Painel Administrativo customizado para gestão dessas mensagens.

## 🚀 Tecnologias Utilizadas

* **Python 3.x**
* **Django 6.0** (Framework Web)
* **Tailwind CSS** (Estilização via CDN)
* **SQLite** (Banco de Dados de desenvolvimento)

## 🛠️ Decisões Técnicas Importantes
* **Arquitetura de Templates:** OrganizEI os templates em uma subpasta `admin/` para separar claramente a interface pública da interface de gestão.
* **Segurança de Rotas:** Utilizei `LoginRequiredMixin` e o decorador `@login_required` para garantir que apenas usuários autenticados acessem os dados dos leads.
* **UX no Dashboard:** Implementei um sistema de filtragem dinâmica (Novas vs. Todas) e uma barra de busca que utiliza objetos `Q` do Django para pesquisas complexas em múltiplos campos (Nome, Empresa, E-mail).
* **Gestão de Estado:** Criei uma lógica automática onde a mensagem é marcada como "Lida" no banco de dados assim que o administrador abre os detalhes da mesma.

## 📦 Instalação e Execução

1️⃣ **Clone o repositório**
```bash
git clone [https://github.com/KamilleXavier/recruiting.git](https://github.com/KamilleXavier/recruiting.git)
cd zaffiro-consultoria

2️⃣ Crie e ative um ambiente virtualBashpython -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

3️⃣ Instale as dependênciasBashpip install -r requirements.txt

4️⃣ Configure o banco de dadosBashpython manage.py makemigrations
python manage.py migrate

5️⃣ Crie um superusuárioBashpython manage.py createsuperuser

6️⃣ Execute o servidorBashpython manage.py runserver

7️⃣ Acesse a aplicaçãoPáginaURLLandpagehttps://www.google.com/search?q=http://127.0.0.1:8000Login Administrativohttps://www.google.com/search?q=http://127.0.0.1:8000/login/Dashboard de Leadshttps://www.google.com/search?q=http://127.0.0.1:8000/dashboard/

Desenvolvido por Kamille Xavier