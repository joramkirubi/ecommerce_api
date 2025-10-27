E-commerce API (Django REST Framework)

A simple E-commerce API built with Django and Django REST Framework.
You can view, add, edit, or delete products through the API or Django admin panel.

Tech Stack

Django 5+

Django REST Framework

SQLite3

Python 3.13.7

How to Run

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/ecommerce_api.git
cd ecommerce_api


2. Create a virtual environment

python -m venv venv


3. Activate the environment

venv\Scripts\activate     # On Windows
source venv/bin/activate  # On macOS/Linux


4. Install dependencies

pip install django djangorestframework


5. Run migrations

python manage.py migrate


6. Create a superuser

python manage.py createsuperuser


7. Start the server

python manage.py runserver

Then go to:
http://localhost:8000/api/products/

| Method | Endpoint              | Description       |
| ------ | --------------------- | ----------------- |
| GET    | `/api/products/`      | List all products |
| POST   | `/api/products/`      | Add a new product |
| GET    | `/api/products/{id}/` | View one product  |
| PUT    | `/api/products/{id}/` | Edit a product    |
| DELETE | `/api/products/{id}/` | Delete a product  |

Example JSON 


{
    "id": 1,
    "name": "Wireless Mouse",
    "description": "A smooth, lightweight mouse perfect for daily use.",
    "price": 19.99,
    "stock": 50,
    "image": "http://localhost:8000/media/products/wireless-mouse.jpg"
}
