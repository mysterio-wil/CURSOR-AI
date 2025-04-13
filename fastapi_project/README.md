# FastAPI Project

This is a basic FastAPI project setup with a proper project structure.

## Project Structure
```
fastapi_project/
├── main.py      # Contiene las rutas de la API
├── settings.py  # Configuración del proyecto
├── requirements.txt
└── README.md
```

## Setup

1. Create a virtual environment and install dependencies:
```bash
cd fastapi_project
python -m venv .venv
.venv\Scripts\activate  # En Windows
pip install -r requirements.txt
```

## Running the Application

To run the application, use:
```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000

You can view the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

- `GET /`: Endpoint principal que muestra un mensaje de bienvenida
- `GET /health`: Endpoint de verificación de salud de la aplicación 