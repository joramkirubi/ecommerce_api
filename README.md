🛍️ E-commerce API (Django REST Framework)
📌 Overview

This is a simple E-commerce API built using Django and Django REST Framework (DRF).
It allows users to:

View a list of products

Create new products (via the API or admin panel)

Manage product details through the Django Admin dashboard

🧩 Features

Django REST Framework-based API

CRUD operations for Products

Admin panel for managing data

SQLite database for easy setup

⚙️ Tech Stack

Backend: Django 5+, Django REST Framework

Database: SQLite3

Language: Python 3.10+

📁 Project Structure
ecommerce_api/
├── api/                 # Contains views, serializers, urls, models
├── ecommerce/           # Main project settings and URLs
├── db.sqlite3           # Local development database
├── manage.py            # Django management file
└── README.md            # Project documentation

🚀 Getting Started
1️⃣ Clone the repository
git clone https://github.com/<your-username>/ecommerce_api.git
cd ecommerce_api

2️⃣ Create and activate virtual environment
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

3️⃣ Install dependencies
pip install django djangorestframework

4️⃣ Run migrations
python manage.py migrate

5️⃣ Create superuser
python manage.py createsuperuser

6️⃣ Start the server
python manage.py runserver

🌐 API Endpoints
Method	Endpoint	Description
GET	/api/products/	List all products
POST	/api/products/	Create a new product
GET	/api/products/{id}/	Retrieve a product
PUT	/api/products/{id}/	Update a product
DELETE	/api/products/{id}/	Delete a product
🔑 Admin Panel

Visit:
👉 http://localhost:8000/admin/

Login with your superuser credentials to manage products easily.

🧾 Example JSON (POST)
{
  "name": "Wireless Mouse",
  "description": "Ergonomic Bluetooth mouse",
  "price": "2500.00"
}

👨‍💻 Author

Joram Kirubi
