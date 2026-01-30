from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["Users"], responses={404: {"message": "Not found"}})

# Entidad User
class User(BaseModel):
    id: int
    name: str
    lastname: str
    age: int

users_list = [User(id=1, name="Frank", lastname="Doe", age=30), 
        User(id=2, name="John", lastname="Doe", age=25), 
        User(id=3, name="Jane", lastname="Doe", age=22)]

@router.get('/json')
async def usersjson():
    return [{"name": "Frank", "lastname": "Doe" ,"age": 30}, 
            {"name": "John", "lastname": "Doe" ,"age": 25}, 
            {"name": "Jane", "lastname": "Doe" ,"age": 22}]

@router.get('/')
async def users():
    return users_list

# Path param
@router.get('/{id}')
async def user(id: int):
    return search_user(id)

# Query param
@router.get('/{id}')
async def user(id: int):
    return search_user(id)

# Post param
@router.post('/', status_code=201)
async def user(user: User):

    existing_user = search_user(user.id)

    if isinstance(existing_user, User):
        # raise se utiliza para indicar que ha ocurrido un error
        raise HTTPException(status_code=404, detail="User already exists")
    
    users_list.append(user)
    return user
    

@router.put('/')
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
        
    if not found:
        return {"error": "User not update"}
    
    return user

@router.delete('/{id}')
async def user(id: int):
    
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "User not delete"}

# Funcion para buscar usuario
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User not found"}



