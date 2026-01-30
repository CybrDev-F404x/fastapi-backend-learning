from fastapi import APIRouter, HTTPException, status
from db.models.user_model import User
from db.clients.client import db_client
from db.schemas.user_sch import user_schema, users_schemas
from bson import ObjectId

router = APIRouter(prefix="/usersdb", tags=["UsersDB"], 
    responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})

users_list = []

@router.get('/', response_model=list[User])
async def users():
    return users_schemas(db_client.find())

# Path param
@router.get('/{id}')
async def user(id: str):
    return search_user_by_field("_id", ObjectId(id))

# Query param
@router.get('/{id}')
async def user(id: str):
    return search_user_by_field("_id", ObjectId(id))

# Post param
@router.post('/', response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):

    existing_user = search_user_by_field("email", user.email)

    if isinstance(existing_user, User):
        # raise se utiliza para indicar que ha ocurrido un error
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User already exists")
    
    # Convertimos el objeto User a diccionario
    user_dict = dict(user)

    # Eliminamos el id porque no lo necesitamos en la base de datos
    del user_dict["id"]

    # Insertamos el usuario en la base de datos y obtenemos el id del usuario insertado
    user_id = db_client.insert_one(user_dict).inserted_id

    # Obtenemos el usuario insertado y lo convertimos a un diccionario 
    new_user = user_schema(db_client.find_one({"_id": user_id}))
    
    return User(**new_user)
    

@router.put('/', response_model=User)
async def user(user: User):

    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)

    except:
        return {"error": "User not update"}
        
    
    return search_user_by_field("_id", ObjectId(user.id))

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    
    found = db_client.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "User not delete"}

# Funcion para buscar usuario por field y key
def search_user_by_field(field: str, key):
    
    try:
        user = user_schema(db_client.find_one({field: key}))
        return User(**user)
    except:
        return {"error": "User not found"}



