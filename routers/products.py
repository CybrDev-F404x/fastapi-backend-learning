from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"], responses={404: {"message": "Not found"}})

products_list = ["Product 1", "Product 2", "Product 3"]

@router.get('/', status_code=200)
async def products():
    return products_list

@router.get('/{id}', status_code=200)
async def products(id: int):
    return products_list[id]


