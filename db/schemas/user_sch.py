
def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"]}

def users_schemas(users) -> list:
    # Convierte una lista de usuarios a una lista de diccionarios
    return [user_schema(user) for user in users]