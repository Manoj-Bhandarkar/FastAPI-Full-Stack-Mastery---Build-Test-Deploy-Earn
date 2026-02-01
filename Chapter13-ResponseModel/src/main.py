from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any

app = FastAPI()

#---------------------------------
# Response Model
#---------------------------------
class Product_Response(BaseModel):
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
@app.get("/products10")
async def get_products10():
  return {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5}

#-------------------------------------
# with response_model Parameter
#-------------------------------------
@app.get("/products11", response_model=Product_Response)
async def get_products11():
  return {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5}

