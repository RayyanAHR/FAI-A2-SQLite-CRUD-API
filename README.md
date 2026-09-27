# FAI-A2: SQLite CRUD API

A lightweight RESTful CRUD API built with **FastAPI**, **SQLAlchemy**, and an embedded **SQLite** database. Designed to demonstrate asynchronous request handling, database session management, and Pydantic validation.

## 🚀 Tech Stack

- **Framework:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Data Validation:** Pydantic
- **Language:** Python 3.10+

## ✨ Features

- **Full CRUD Operations:** Support for Create, Read, Update, and Delete endpoints.
- **Embedded Database:** Zero-config SQLite database setup for local development.
- **Automatic API Docs:** Interactive OpenAPI / Swagger UI generated at `/docs`.
- **Validation:** Strict request and response schemas using Pydantic models.

## 🛠️ Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/RayyanAHR/FAI-A2-SQLite-CRUD-API.git](https://github.com/RayyanAHR/FAI-A2-SQLite-CRUD-API.git)
cd FAI-A2-SQLite-CRUD-API

```

### 2. Set up virtual environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Run the API server

```bash
uvicorn app.main:app --reload

```

Access interactive documentation at `http://127.0.0.1:8000/docs`.

```

```
