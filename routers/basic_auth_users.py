from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/basic_auth", tags=["Basic Auth"], 
    responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Entidad User
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "Cybr": {
        "username": "Cybr",
        "full_name": "Frank",
        "email": "frank@frank.com",
        "disabled": False,
        "password": "1234"
    }, 
    "Cybr2": {
        "username": "Cybr2",
        "full_name": "Frank",
        "email": "frank2@frank.com",
        "disabled": True,
        "password": "12345"     
    },
    "Cybr3": {
        "username": "Cybr3",
        "full_name": "Frank",
        "email": "frank3@frank.com",
        "disabled": False,
        "password": "123456"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Invalid authentication credentials", 
        headers={"WWW-Authenticate": "Bearer"})
    
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
        detail="Inactive user")

    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_dict = users_db.get(form.username)

    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect user")

    if not form.password == user_dict["password"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")

    return {"access_token": user_dict["username"], "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user