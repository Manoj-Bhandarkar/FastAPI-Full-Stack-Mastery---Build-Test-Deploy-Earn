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
class Product_Nested(BaseModel):
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
async def create_product_nested_body_model(product: Product_Nested):
    return product

#-----------------------------
## Attributes with lists of submodels
#-----------------------------
class Category_list(BaseModel):
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
    category: list[Category_list] | None = Field(
       default=None,
       title="Product Category",
       description="The category to which the product belongs"
    )

@app.post("/product3")
async def create_product_list_model(product: Product):
    return product
#=======================================================================
#-----------------------------
## Field-level Examples - using Example - for understand what value expected in json 
#-----------------------------
class Product_Example(BaseModel):
    name: str = Field(examples=["Moto E"])
    price: float = Field(examples=[23.56])
    stock: int | None = Field(default=None, examples=[43])

@app.post("/product4")
async def create_product_field_exaple_example(product: Product_Example):
    return product

#-----------------------------
## Field-level Examples - Using Pydantic’s json_schema_extra - for understand what value expected in json
#-----------------------------

class Product_json_scheme_extra(BaseModel):
  name: str
  price: float
  stock: int | None = None

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "name": "Moto E",
          "price": 34.56,
          "stock": 45
        }
      ]
    }
  }

@app.post("/product5")
async def create_product_field_exaple_json_schema_extra(product: Product_json_scheme_extra):
    return product