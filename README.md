E-commerce API (Django REST Framework)

Overview

This is a simple E-commerce API built with Django and Django REST Framework (DRF).
It lets you view, add, edit, and delete products through API endpoints or the Django admin panel.

Tech Stack

Backend: Django 5+, Django REST Framework

Database: SQLite3

Language: Python 3.10+

📁 Project Structure
ecommerce_api/
│
├── api/           # API app (models, views, serializers, urls)
├── ecommerce/     # Main project (settings and urls)
├── db.sqlite3     # Local SQLite database
├── manage.py      # Django management script
└── README.md      # This file

 How to Run the Project
 Clone the repository
git clone https://github.com/YOUR-USERNAME/ecommerce_api.git
cd ecommerce_api

 Create a virtual environment
python -m venv venv


Activate it:

venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux

 Install dependencies
pip install django djangorestframework

 Run migrations
python manage.py migrate

 Create superuser
python manage.py createsuperuser

 Start the server
python manage.py runserver


Now open this in your browser:
 http://localhost:8000/api/products/

 API Endpoints
Method	Endpoint	Description
GET	/api/products/	List all products
POST	/api/products/	Add a new product
GET	/api/products/{id}/	View one product
PUT	/api/products/{id}/	Edit a product
DELETE	/api/products/{id}/	Delete a product

 Example JSON (for POST)
{
  "name": "Wireless Mouse",
  "description": "Bluetooth mouse with long battery life",
  "price": "2500.00",
  "category": "Electronics",
  "stock_quantity": 30,
  "image_url": "https://example.com/mouse.jpg"
}

 Admin Panel

Manage all products through the admin dashboard:
 http://localhost:8000/admin/

Use your superuser login credentials.

Author

Joram Kirubi
E-commerce API – ALX Final Project
