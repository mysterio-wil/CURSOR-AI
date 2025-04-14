# FastAPI Restaurant API

Una API RESTful simple construida con FastAPI para gestionar un menú de restaurante.

## Características

- ✅ CRUD completo para platos del menú
- ✅ Validación de datos con Pydantic
- ✅ Documentación automática con Swagger UI y ReDoc
- ✅ Configuración basada en variables de entorno
- ✅ Base de datos en memoria para demostración
- ✅ CORS habilitado para desarrollo frontend

## Estructura del Proyecto

```
fastapi_project/
├── app/
│   ├── main.py         # Punto de entrada de la aplicación
│   ├── schemas.py      # Modelos Pydantic
│   └── settings.py     # Configuración de la aplicación
├── .env                # Variables de entorno
├── .gitignore         # Archivos ignorados por git
├── requirements.txt    # Dependencias del proyecto
└── pyproject.toml     # Configuración de herramientas de desarrollo
```

## Requisitos

- Python 3.11+
- Dependencias listadas en `requirements.txt`

## Configuración

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd fastapi_project
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Copiar variables de entorno:
```bash
cp .env.example .env
```

5. Iniciar la aplicación:
```bash
python -m uvicorn app.main:app --reload
```

## Documentación de la API

La API está documentada automáticamente y puede ser accedida en:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoints Disponibles

### GET /
Mensaje de bienvenida y versión de la aplicación.

### GET /health
Verificación del estado de la aplicación.

### GET /dishes
Lista todos los platos disponibles.

### GET /dishes/{dish_id}
Obtiene un plato específico por su ID.

## Pruebas de la API

Puedes probar la API de varias formas:

1. **Usando la Documentación Interactiva**
   - Visita http://127.0.0.1:8000/docs
   - Haz clic en cualquier endpoint
   - Usa el botón "Try it out"

2. **Usando curl**
```bash
# Obtener todos los platos
curl http://127.0.0.1:8000/dishes

# Obtener un plato específico
curl http://127.0.0.1:8000/dishes/1
```

3. **Usando herramientas como Postman**
   - Importa la especificación OpenAPI desde /docs
   - Crea y guarda tus peticiones

## Desarrollo

### Herramientas Utilizadas
- FastAPI 0.109.2
- Pydantic 2.6.1
- Uvicorn 0.27.1
- SQLAlchemy 2.0.25
- Ruff 0.3.0 (linter y formateador)

### Convenciones de Código
- PEP 8 para estilo de código
- Type hints en todas las funciones
- Documentación con docstrings
- Validación de datos con Pydantic

## Contribución

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles. 