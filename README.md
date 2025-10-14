E-commerce API (Django REST Framework)
Overview

This is a simple E-commerce API built with Django and Django REST Framework (DRF).
It allows you to view, add, edit, and delete products through API endpoints or the Django admin panel.

Tech Stack

Backend: Django 5+, Django REST Framework

Database: SQLite3

Language: Python 3.10+

📁 Project Structure
ecommerce_api/
│
├── api/              # API app (models, views, serializers, urls)
├── ecommerce/        # Main project (settings and urls)
├── db.sqlite3        # Local SQLite database
├── manage.py         # Django management script
└── README.md         # This file

⚙️ How to Run the Project

Clone the repository:

git clone https://github.com/YOUR-USERNAME/ecommerce_api.git
cd ecommerce_api


Create a virtual environment:

python -m venv venv


Activate it:

venv\Scripts\activate    # On Windows
source venv/bin/activate # On macOS/Linux


Install dependencies:

pip install django djangorestframework


Run migrations:

python manage.py migrate


Create superuser:

python manage.py createsuperuser


Start the server:

python manage.py runserver


Then open this in your browser:
👉 http://localhost:8000/api/products/

🧩 API Endpoints
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

🧪 API Testing (Postman)

After setting up the views and URLs, I tested all endpoints using Postman to confirm everything works correctly.

1️⃣ Base URL
http://127.0.0.1:8000/api/products/

2️⃣ GET Request – View All Products

I selected the GET method and entered the base URL.
The response returned all products in the database.

✅ Response Example:

{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 3,
      "name": "MacBook Air M2",
      "description": "Apple MacBook Air with M2 chip, 8GB unified memory, 256GB SSD storage, 13.6-inch Retina display, and all-day battery life.",
      "price": "175000.00",
      "category": "Electronics",
      "stock_quantity": 10,
      "image_url": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-m2-midnight-select-202206",
      "created_at": "2025-10-14T16:26:43.080960Z"
    },
    {
      "id": 2,
      "name": "Samsung Galaxy S24",
      "description": "Latest Samsung flagship smartphone with 256GB storage and 8GB RAM.",
      "price": "150000.00",
      "category": "Electronics",
      "stock_quantity": 25,
      "image_url": "https://images.samsung.com/is/image/samsung/p6pim/africa_en/galaxy-s24/gallery/galaxy-s24-highlights-kv-01-720.jpg",
      "created_at": "2025-10-14T13:47:48.446154Z"
    },
    {
      "id": 1,
      "name": "iPhone 15",
      "description": "Apple smartphone, 128GB",
      "price": "150000.00",
      "category": "Electronics",
      "stock_quantity": 10,
      "image_url": "",
      "created_at": "2025-10-11T17:56:09.230650Z"
    }
  ]
}


It showed all 3 products, confirming the GET endpoint works.

3️⃣ Filters, Search & Ordering

To test search and filtering features, I used these examples:

Feature	Example URL
Filter by category	/api/products/?category=Electronics
Search by name	/api/products/?search=Samsung
Order by price	/api/products/?ordering=price

All of them worked as expected and returned the right products.

✅ Summary

Everything works as expected:

GET all products

GET by ID

Filtering, searching, and ordering

The API is now fully functional and ready to connect with the frontend.

🧭 Admin Panel

You can also manage products through the Django admin dashboard:
👉 http://localhost:8000/admin/

Use your superuser credentials to log in.

Author

Joram Kirubi
E-commerce API – ALX Final Project
