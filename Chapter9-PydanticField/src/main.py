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

#-----------------------------
# ## Nested Body Models
## Submodel
#-----------------------------
class Category(BaseModel):
  name : str = Field(
    title="Category Name",
    description="The name of the product category",
    max_length=50,
    min_length=1
  )
  description: str | None = Field(
        default=None,
        title="Category Description",
        description="A brief description of the category",
        max_length=200
    )
  
## Model which will use Submodel
class Product(BaseModel):
    name: str = Field(
        title="Product Name",
        description="The name of the product",
        max_length=100,
        min_length=1
    )
    price: float = Field(
        gt=0,
        title="Product Price",
        description="The price in USD, must be greater than zero"
    )
    stock: int | None = Field(
        default=None,
        ge=0,
        title="Stock Quantity",
        description="Number of items in stock, must be non-negative"
    )
    category : Category | None = Field(
       default=None,
       title="Product Category",
       description="The category to which the product belongs"
    )

@app.post("/product2")
async def create_product_nested_body_model(product: Product):
    return product

#-----------------------------
## Attributes with lists of submodels
#-----------------------------
class Category(BaseModel):
    name: str = Field(
        title="Category Name",
        description="The name of the product category",
        max_length=50,
        min_length=1
    )
    description: str | None = Field(
        default=None,
        title="Category Description",
        description="A brief description of the category",
        max_length=200
    )

class Product(BaseModel):
    name: str = Field(
        title="Product Name",
        description="The name of the product",
        max_length=100,
        min_length=1
    )
    price: float = Field(
        gt=0,
        title="Product Price",
        description="The price in USD, must be greater than zero"
    )
    stock: int | None = Field(
        default=None,
        ge=0,
        title="Stock Quantity",
        description="Number of items in stock, must be non-negative"
    )
    category: list[Category] | None = Field(
       default=None,
       title="Product Category",
       description="The category to which the product belongs"
    )

@app.post("/product3")
async def create_product_list_model(product: Product):
    return product