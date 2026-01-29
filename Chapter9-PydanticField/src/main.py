from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()

#-----------------------------
## Pydantic’s Field
#-----------------------------
class Product_field(BaseModel):
  name: str = Field(
    title="Product Name",
    description="The name of the product",
    max_length=100,
    min_length=3,
    pattern="^[A-Za-z0-9 ]+$"
  )
  price: float = Field(
    gt=0,
    title="Product Price",
    description="The price of the product in USD, must be greater than zero"
  )
  stock: int | None = Field(
    default=None,
    ge=0,
    title="Stock Quantity",
    description="The number of items in stock, must be non-negative"
  )

@app.post("/product1")
async def create_product_field(product: Product_field):
  return product
