# 📝 Django TODO Application

A simple yet complete **CRUD-based TODO application** built using **Django**.  
This project demonstrates clean architecture, Django best practices, class-based views, forms, templates, and includes **full test coverage** for the core functionality.

This repository was created while working through an AI-assisted development workflow.  
The original prompt used to generate this project is included at the bottom of this README for transparency.

---

## 🚀 Features

### ✅ Core TODO Management  
- Create TODO items  
- Edit existing TODOs  
- Delete TODOs  
- Assign due dates (`datetime-local` browser input)  
- Mark TODOs as resolved / unresolved  

### 🖥 User Interface  
- Bootstrap-powered UI  
- Crispy Forms (`crispy-bootstrap5`) integration  
- Clean and minimal layout  
- Table view, Detail view, Form view, Delete confirmation  

### 🧪 Test Coverage  
Full test suite includes:
- Model tests  
- Form validation tests  
- View tests (CRUD + toggle resolved)  
- Integration test using Django test client  

### 🧱 Architecture / Patterns  
- Django Class-Based Views (List, Create, Update, Delete, Detail)  
- ModelForm for handling data  
- namespaced URL architecture  
- Template inheritance with a base layout  
- Separate `todos` app for clean modular design  

---

## 🏗 Tech Stack

| Component | Technology |
|----------|------------|
| Backend | Django 5.x |
| Frontend | Bootstrap 5 via CDN |
| Forms | django-crispy-forms + crispy-bootstrap5 |
| Database | SQLite (default) |
| Server | Django runserver (optional: Uvicorn ASGI) |
| Testing | Django TestCase, Test Client |
| Version Control | Git + GitHub |

---

## 📦 Project Setup

Follow these steps to run the project locally.

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/dipaksaraf/YOUR-REPO.git
cd YOUR-REPO

2️⃣ Create Virtual Environment
python -m venv .venv

Activate it:

Mac / Linux:

source .venv/bin/activate


Windows (PowerShell):

.venv\Scripts\Activate.ps1

3️⃣ Install Dependencies
pip install -r requirements.txt


If you don’t have a requirements.txt, generate one:

pip freeze > requirements.txt

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Start Server
python manage.py runserver


Your app is now available at:

👉 http://127.0.0.1:8000/

🧪 Running Tests

This project includes a full test suite covering:

Models
Forms
CRUD Views
Toggle-resolved behavior

Run all tests:

python manage.py test


Verbose mode:

python manage.py test -v 2

📁 Project Structure
django-todo/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── todos/
│   ├── migrations/
│   ├── templates/todos/
│   │   ├── base.html
│   │   ├── todo_list.html
│   │   ├── todo_detail.html
│   │   ├── todo_form.html
│   │   └── todo_confirm_delete.html
│   ├── tests.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
└── README.md

🤖 Original Prompt (As Requested)

This repository was created based on the following user request:

*“We will build a TODO application in Django.
The app should be able to do the following:

Create, edit and delete TODOs

Assign due dates

Mark TODOs as resolved
You will only need Python to get started (we also recommend that you use uv).
Give me step by step process on how to setup the environment and proceed with this To Do App.”*

🤝 Contribution

Pull requests are welcome.
For major changes, please open an issue first to discuss your proposal.

📜 License

This project is open-source.