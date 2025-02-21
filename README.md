# Portfolio MSANTOS - Backend

## Description
This repository contains the backend API for my portfolio, developed with Django REST Framework (DRF). The API provides data for the frontend, built with Next.js, ensuring an efficient and secure integration between the project's layers. The backend is configured to receive and provide content in three languages: Portuguese (pt), English (en), and Spanish (es).

## Technologies Used
- **Python 3**
- **Django**
- **Django REST Framework (DRF)**
- **JWT Authentication**
- **SQLite3**

## Project Structure
```
backend/
│── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── languagemid.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
│── core/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
│── projectsimages/
│── venv/
│── .env
│── .gitignore
│── .pylintrc
│── db.sqlite3
│── manage.py
│── README.md
```

## Setup and Execution
### 1. Clone the repository
```sh
git clone https://github.com/msantosdevlab/portfolio_msantos_backend
cd portfolio_msantos_backend
```

### 2. Create and activate a virtual environment
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project's root directory and define the necessary variables. Ensure that **CORS_ALLOWED_ORIGINS** includes the allowed frontend URLs, for example:
```sh
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

### 5. Apply migrations
```sh
python manage.py migrate
```

### 6. Create a superuser (to access Django Admin and generate an access token)
```sh
python manage.py createsuperuser
```

### 7. Start the server
```sh
python manage.py runserver
```
The server will be available at `http://127.0.0.1:8000/`.

## API Endpoints
Currently, the API has one main endpoint:

### **Get Portfolio Content**
- **Route:** `/content/`
- **Method:** `GET`
- **Authentication:** JWT (authenticated users only)
- **Parameters:** `lang` (optional, sets the response language. Default: `pt`)
- **Response:**
```json
{
    "menu": [...],
    "introduction": {...},
    "project_content": {...},
    "project_categories": [...],
    "projects": [...],
    "linkedin": {...},
    "contact": {...},
    "footer": {...}
}
```

## Authentication
After creating the superuser for your Django project, you can generate the access token needed to authenticate requests to protected endpoints. Follow these steps to generate the token:

### Step 1: Create the Superuser
If you haven't created a superuser yet, run the following command in the terminal:
```sh
python manage.py createsuperuser
```
Fill in the required fields to create an admin user.

### Step 2: Generate the Access Token
After creating the superuser, send a POST request to the `/api/token/access/` endpoint using Postman or any other HTTP client.

In the request body (Body), send a JSON object containing the username and password of the superuser you just created. Example:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```
Upon sending the request, you will receive a response containing the access token:
```json
{
  "access": "your_access_token_here"
}
```

### Step 3: Use the Token in Requests
To access protected API endpoints, add the generated access token in the Authorization header of your requests. The header format is:
```sh
Authorization: Bearer your_access_token_here
```
Example in Postman:

Headers:
```sh
Auth Type: Bearer Token
Token: insert your token
```

**Feel free to review and suggest improvements!** 😊

