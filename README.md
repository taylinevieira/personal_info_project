# Personal Info API 🧠

Este é um projeto Django desenvolvido como exercício para praticar rotas, views, templates, CBVs e manipulação de parâmetros em URLs e query strings.

## 🔧 Tecnologias Utilizadas
- Python 3.13+
- Django 5.2+
- HTML (para templates)
- JSON (como formato de resposta das views)

## 🚀 Funcionalidades Implementadas

### 🟢 Parte 1 — Rotas Simples
- `/welcome` → Retorna uma mensagem de boas-vindas (JSON)
- `/goodbye` → Retorna uma mensagem de despedida (JSON)
- `/current-time` → Retorna a hora atual no formato `HH:MM:SS` (JSON)

### 🟡 Parte 2 — Rotas com Lógica Progressiva
- `/greet?name=SeuNome` → Retorna “Hello, <name>!” ou “Hello, Stranger!” se o parâmetro não for informado
- `/age-category?age=XX` → Retorna a categoria: Child, Teenager, Adult ou Senior
- `/sum/<num1>/<num2>` → Soma dois números inteiros passados na URL

### 🧩 Parte Avançada — Técnicas
- Views migradas para **Class-Based Views**: `/welcome`, `/goodbye`
- View `/about` renderiza um **template HTML** com nome, descrição e ano atual
- Model `Person` com campos `name` (CharField) e `age` (IntegerField)
- View `/people` retorna todos os registros do model em JSON
- Admin do Django configurado para gerenciar `Person`

## 🗂️ Como Rodar o Projeto

```bash
# 1. Clone o repositório
git clone https://github.com/taylinevieira/personal_info_project.git
cd personal_info_project

# 2. Crie e ative o ambiente virtual
python -m venv venv
.\venv\Scripts\Activate  # Para PowerShell no Windows

# 3. Instale as dependências
pip install django

# 4. Execute as migrações e crie um superusuário
python manage.py migrate
python manage.py createsuperuser

# 5. Inicie o servidor
python manage.py runserver
