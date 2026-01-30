from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
  id: int
  name: str
  price : float
  stock: int | None = None

#-------------------------
# # Without Return Type
#-------------------------
@app.get("/products1")
async def get_products1():
    return [
       {"status": "OK"},
       {"status": 200}
    ]

#-------------------------
## Return type - pydantic model as return type
#-------------------------
@app.get("/products2")
async def get_product_pydantic_return() -> Product:
    return {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5}

@app.get("/products3/")
async def get_products3() -> Product:
    return {"id": 1, "name": "Moto E", "price": 33.44}

@app.get("/products4")
async def get_products3() -> Product:
    return {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5, "description": "This is moto e"}

@app.get("/products5")
async def get_products5() -> List[Product]:
    return [
       {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5},
       {"id": 2, "name": "Redmi 4", "price": 55.33, "stock": 7}
    ]

@app.get("/products6")
async def get_products6() -> List[Product]:
    return [
       {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5, "description": "Hello Desc1"},
       {"id": 2, "name": "Redmi 4", "price": 55.33, "stock": 7, "description": "Hello Desc2"}
    ]
#-------------------------------
## Accept one Pydantic and return other Pydantic - with Post Method 
#-------------------------------
class ProductOut(BaseModel):
  name: str
  price : float

@app.post("/products7")
async def create_product7(product: Product) -> Product:
  return product

@app.post("/products8")
async def create_product8(product: Product) -> ProductOut:
  return product

class BaseUser(BaseModel):
    username: str
    full_name: str | None = None

class UserIn(BaseUser):
    password: str

@app.post("/users9")
async def create_user(user: UserIn) -> BaseUser:
  return user