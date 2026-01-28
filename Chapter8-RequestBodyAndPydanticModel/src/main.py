from fastapi import FastAPI, Body
from pydantic import BaseModel
app = FastAPI()
from typing import Annotated

## Without Pydantic
## Create or Insert Data
@app.post("/product1")
async def create_product(new_product: dict):
    return new_product


## With Pydantic
# # Define the Product model
class Product_pydandic(BaseModel):
  id: int
  name: str
  price: float
  stock: int | None = None

@app.post("/product2")
async def create_product_with_pydantic(new_product: Product_pydandic):
  return new_product

# ## Access Attribute inside Function
@app.post("/product3")
async def product_fetch_pydantic_value(new_product: Product_pydandic):
  print(new_product.id)
  print(new_product.name)
  print(new_product.price)
  print(new_product.stock)
  return new_product

#---------------------------------
## Add new calculated attribute
#---------------------------------
@app.post("/product4")
async def create_product_calculation_on_attribute(new_product: Product_pydandic):
  product_dict = new_product.model_dump()
  price_with_tax = new_product.price + (new_product.price * 18 / 100)
  product_dict.update({"price_with_tax": price_with_tax})
  return product_dict

#---------------------------------
## Combining Request Body with Path Parameters
#---------------------------------
@app.put("/products5/{product_id}")
async def update_product_requestbody_with_pathparam(product_id: int, new_updated_product: Product_pydandic):
    return {"product_id": product_id, "new_updated_product":new_updated_product}

#---------------------------------
## Adding Query Parameters
#---------------------------------
@app.put("/products6/{product_id}")
async def update_product_with_queryparam(product_id: int, new_updated_product: Product_pydandic, discount: float | None = None):
    return {"product_id": product_id, "new_updated_product": new_updated_product, "discount": discount}
#====================================================================================================
#---------------------------------
## Multiple Request Body Parameters
#---------------------------------
class Pydantic_Product(BaseModel):
  name: str
  price:float
  stock: int | None = None
class Pydantic_Seller(BaseModel):
  username: str
  full_name: str | None = None

@app.post("/product7")
async def create_product_with_muli_pydantic(product: Pydantic_Product, seller:Pydantic_Seller):
  return {"product": product, "seller":seller}

#---------------------------------
## Make Body Optional
#---------------------------------
@app.post("/product8")
async def create_product_pydantic_optional(product: Pydantic_Product, seller:Pydantic_Seller | None = None):
  return {"product": product, "seller":seller}

#---------------------------------
## Singular values in body
#---------------------------------
@app.post("/product9")
async def create_product_singleValue_reqbody(
  product: Pydantic_Product, 
  seller:Pydantic_Seller, 
  sec_key: Annotated[str, Body()]
  ):
  return {"product": product, "seller":seller, "sec_key":sec_key}

#---------------------------------
## Embed a single body parameter
#---------------------------------
# Without Embed
@app.post("/product10")
async def create_product_Without_Embed(product: Pydantic_Product):
  return product

#---------------------------------
## With Embed
#---------------------------------
@app.post("/product11")
async def create_product_With_Embed(product: Annotated[Pydantic_Product, Body(embed=True)]):
  return product