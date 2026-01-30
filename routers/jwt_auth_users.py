from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt.exceptions import PyJWTError
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher
from pwdlib.hashers.bcrypt import BcryptHasher
from datetime import datetime, timedelta, timezone

# Configuracion
algorithm_jwt = "HS256"
access_token_duration = 1
secret_key_jwt = "bd41dac1d6a96a973454780146cf8f4a35d5e8f54b269c61e3509dd1e4a17163"

router = APIRouter(prefix="/jwt_auth", tags=["JWT Auth"], 
    responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})

# OAuth2
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Password hash
password_hash = PasswordHash(hashers=[Argon2Hasher(), BcryptHasher()])

# Entidad User
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

# Entidad UserDB
class UserDB(User):
    password: str

users_db = {
    "Cybr": {
        "username": "Cybr",
        "full_name": "Frank",
        "email": "frank@frank.com",
        "disabled": False,
        "password": "$2a$12$nmRSRX9x76FiCqLOqQFmbOuleINdnqXF9FtxgNXazb10iCfLbErUK"
    }, 
    "Cybr2": {
        "username": "Cybr2",
        "full_name": "Frank",
        "email": "frank2@frank.com",
        "disabled": True,
        "password": "$2a$12$JvmyNc4sQlncRWlQetmzYOBzfjcQddgwrR31DtD7FE8iJhJuyamom"     
    },
    "Cybr3": {
        "username": "Cybr3",
        "full_name": "Frank",
        "email": "frank3@frank.com",
        "disabled": False,
        "password": "$2a$12$7RwGF2hxDv.7vfvovnKk0O8aeSbo78oqvdJI.r7Wsmjj8EIzVO3jG"
    }
}

# Buscar usuario en la base de datos
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

# Buscar usuario
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

# Autenticar usuario
async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid authentication credentials", 
            headers={"WWW-Authenticate": "Bearer"})
    
    try:
        username = jwt.decode(token, secret_key_jwt, algorithms=[algorithm_jwt]).get("sub")
        if username is None:
            raise exception

    except PyJWTError:
        raise exception

    return search_user(username)

# Usuario actual
async def current_user(user: User = Depends(auth_user)):

    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
        detail="Inactive user")

    return user

# Login
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_dict = users_db.get(form.username)
    
    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect user")

    if not password_hash.verify(form.password, user_dict["password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")

    access_token_expires = datetime.now(timezone.utc) + timedelta(minutes=access_token_duration)
    access_token = {"sub": user_dict["username"], "exp": access_token_expires}

    return {"access_token": jwt.encode(access_token, secret_key_jwt, algorithm=algorithm_jwt), "token_type": "bearer"}

# Mi usuario
@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user