# FastAPI Backend Learning

Este repositorio contiene un backend completo construido con **FastAPI** y **Python**, desarrollado como parte de un proceso de aprendizaje.

El proyecto incluye ejemplos prácticos de creación de una API RESTful, integración con bases de datos NoSQL (MongoDB) y sistemas de autenticación robustos.

## 🌐 Despliegue en Vivo

El proyecto se encuentra desplegado y funcional en la siguiente URL: 👉([https://fastapi-backend-learning.vercel.app/](https://fastapi-backend-learning.vercel.app/))

## 🚀 Características

- **API RESTful**: Endpoints estructurados y documentados automáticamente.
- **Base de Datos**: Integración con **MongoDB** usando `pymongo` (versión local y remota).
- **Autenticación**:
  - 🔐 **Basic Auth**: Autenticación básica.
  - 🔑 **JWT Auth (OAuth2)**: Autenticación segura basada en tokens con hashing de contraseñas (Bcrypt/Argon2).
- **Validación de Datos**: Modelos robustos utilizando **Pydantic**.
- **Documentación Interactiva**: Swagger UI y ReDoc integrados.

## 🛠️ Tecnologías Utilizadas

- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) - Framework web moderno y rápido.
- [MongoDB](https://www.mongodb.com/) - Base de datos NoSQL.
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI.
- [PyJWT](https://pyjwt.readthedocs.io/) - Gestión de JSON Web Tokens.
- [Passlib](https://passlib.readthedocs.io/) - Hashing de contraseñas.

## ⚙️ Instalación Local

### 1. Clonar el repositorio

```bash
git clone https://github.com/CybrDev-F404x/fastapi-backend-learning.git
cd fastapi-backend-learning
```

### 2. Crear un entorno virtual

```bash
python -m venv .venv
# En Windows:
.venv\Scripts\activate
# En Mac/Linux:
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto basándote en el siguiente ejemplo.
**Nota:** Necesitarás tu propia URI de conexión a MongoDB.

```env
MONGODB_URI=tu_uri_de_mongodb_atlas
```

## ▶️ Ejecución

Para iniciar el servidor de desarrollo local:

```bash
uvicorn main:app --reload
```

El servidor se iniciará en `http://127.0.0.1:8000`.

## 📚 Documentación de la API

FastAPI genera documentación automática e interactiva. Una vez que el servidor esté corriendo, puedes acceder a ella en:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📂 Estructura del Proyecto

- `main.py`: Punto de entrada de la aplicación.
- `routers/`: Definición de las rutas de la API (usuarios, productos, auth).
- `db/`: Lógica de base de datos (cliente, modelos, esquemas).
- `static/`: Archivos estáticos.
