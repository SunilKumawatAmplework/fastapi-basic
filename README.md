# FastAPI Application

A modern, high-performance REST API built using FastAPI.

---

## 🚀 Features

- FastAPI framework
- RESTful API structure
- Automatic API documentation (Swagger & ReDoc)
- Environment-based configuration
- Scalable project structure

---

## 📦 Requirements

```
- Python 3.10+
- pip
```

---

## 📁 Project Structure

```
project/
│── app/
│ ├── main.py
│ ├── routes/
│ ├── models/
│ ├── schemas/
│ ├── services/
│ └── config.py
│
│── tests/
│── requirements.txt
│── .env
│── README.md

---

```

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/yourusername/your-project-name.git

cd your-project-name

### 2. Create virtual environment

```
python -m venv venv

```

Activate virtual environment:

```
Mac/Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

```
Create a `.env` file in the root directory:

DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## ▶️ Run the Application

```
uvicorn app.main:app --reload

Application will be available at:

http://127.0.0.1:8000
```

---

## 📖 API Documentation

```
FastAPI provides automatic API documentation:

- Swagger UI:
  `http://127.0.0.1:8000/docs`

- ReDoc:
  `http://127.0.0.1:8000/redoc`

---
```

## 🧪 Run Tests

pytest

---

## 🐳 Docker (Optional)

Build Docker image:

docker build -t fastapi-app .

Run Docker container:

docker run -p 8000:8000 fastapi-app

---

## 📄 License

MIT License
# fastapi-basic
