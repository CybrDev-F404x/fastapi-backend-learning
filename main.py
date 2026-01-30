from fastapi import FastAPI
from routers import users, products, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles 

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(users_db.router)

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

# URL local: /
@app.get('/')
async def root():
    return "Hola fastapi"

# URL local: /url
@app.get('/url')
async def url():
    return {"message": "Hola fastapi"}