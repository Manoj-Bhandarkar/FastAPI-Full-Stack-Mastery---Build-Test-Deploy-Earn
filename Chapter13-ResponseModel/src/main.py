from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any

app = FastAPI()

#---------------------------------
# Response Model
#---------------------------------
class Product(BaseModel):
  id: int
  name: str
  price : float
  stock: int | None = None

class ProductOut(BaseModel):
  name: str
  price : float

#-------------------------------------
## without response_model Parameter
#-------------------------------------
@app.get("/products1")
async def get_products1():
  return {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5}

#-------------------------------------
# with response_model Parameter
#-------------------------------------
@app.get("/products2", response_model=Product)
async def get_products2():
  return {"id": 1,  "price": 33.44, "stock": 5}

#-------------------------------------
#  response_model Parameter with List of return
#-------------------------------------
@app.get("/products3", response_model=List[Product])
async def get_products():
  return [
       {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5},
       {"id": 2, "name": "Redmi 4", "price": 55.33, "stock": 7}
    ]

#-------------------------------------
#  response_model Parameter - Not accept Extra field
#-------------------------------------
@app.get("/products4", response_model=List[Product])
async def get_products4():
  return [
       {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5, "description": "Hello Desc1"},
       {"id": 2, "name": "Redmi 4", "price": 55.33, "stock": 7, "description": "Hello Desc2"}
    ]

#-------------------------------------
# Return only Object - Pydantic or json
#-------------------------------------
@app.post("/products5", response_model=Product)
async def create_product5(product: Product):
  return {"id": 2, "name": "Redmi 4", "price": 55.33, "stock": 7}