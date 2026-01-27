from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

PRODUCTS = [
    {
        "id": 1,
        "title": "Ravan Backpack",
        "price": 109.95,
        "description": "Perfect for everyday use and forest walks.",
    },
    {
        "id": 2,
        "title": "Slim Fit T-Shirts",
        "price": 22.3,
        "description": "Comfortable, slim-fitting casual shirts.",
    },
    {
        "id": 3,
        "title": "Cotton Jacket",
        "price": 55.99,
        "description": "Great for outdoor activities and gifting.",
    },
]

#-------------------------------------
# Basic Query Parameter
#-------------------------------------
@app.get("/products")
async def get_products_basic(search : str | None= None):
    if search:
        search_lower = search.lower()
        filtered_products = []
        for product in PRODUCTS :
            if search_lower in product["title"].lower():
                filtered_products.append(product)
        return filtered_products
    return PRODUCTS

#-------------------------------------
# #Validation without Annotated
#-------------------------------------
@app.get("/products")
async def get_products_valid_no_anootation(search: str | None = Query(default=None, max_length=5)):
    if search:
        search_lower = search.lower()
        filtered_products = []
        for product in PRODUCTS:
            if search_lower in product["title"].lower():
                filtered_products.append(product)
        return filtered_products
    return PRODUCTS

#-------------------------------------
# Validation with Annotated ************
#-------------------------------------
@app.get("/products")
async def get_products_annoted_valid(search: Annotated[ str | None, Query(max_length=5)] = None):
  if search:
    search_lower = search.lower()
    filtered_products = []
    for product in PRODUCTS:
      if search_lower in product["title"].lower(): 
        filtered_products.append(product)
    return filtered_products
  return PRODUCTS

# Why use Annotated
## Clear separation of the type
## Better support in some editors and tools for showing metadata and validations directly in the type hints
## Requires Python 3.9+ and FastAPI 0.95+; more modern and recommended approach
## FastAPI 0.95+ officially recommends using Annotated for dependencies and parameters

#-------------------------------------
# Annotated Validation with Required Parameter  - min=3, max=no-limit
#-------------------------------------
@app.get("/products/")
async def get_products_annoted_required_param(search: Annotated[str, Query(min_length=3)]):
    if search:
        search_lower = search.lower()
        filtered_products = []
        for product in PRODUCTS:
            if search_lower in product["title"].lower():
                filtered_products.append(product)
        return filtered_products
    return PRODUCTS

#-------------------------------------
# Annotated Validation with Regular Expression 
# -------------------------------------
@app.get("/products/")
async def get_products_regular_expression (search: Annotated[str | None, Query(min_length=3, pattern="^[a-z]+$")]=None):
    if search:
        search_lower = search.lower()
        filtered_products = []
        for product in PRODUCTS:
            if search_lower in product["title"].lower():
                filtered_products.append(product)
        return filtered_products
    return PRODUCTS


