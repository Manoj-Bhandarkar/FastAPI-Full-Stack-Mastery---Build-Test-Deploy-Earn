from fastapi import FastAPI
from enum import Enum
app = FastAPI()


# @app.get("/product")
# async def all_products():
#     return {"response": "All products"}


# @app.get("/product/{product_id}")
# async def single_products(product_id: int):
#     return {"response": "Single products", "product_id": product_id}

# @app.post("/product")
# async def create_products(new_product: dict):
#     return {"response": "Product Created", "new product": new_product}

# @app.put("/product/{product_id}")
# async def update_products(new_updated_product: dict, product_id: int):
#     return {"response": "Complete Product Updated", "product_id":product_id, "new updated product": new_updated_product}


# @app.patch("/product/{product_id}")
# async def partial_update_products(new_updated_product: dict, product_id: int):
#     return {"response": "Partial Product Updated", "product_id":product_id, "new updated product": new_updated_product}

# @app.delete("/product/{product_id}")
# async def delete_products(product_id: int):
#     return {"response": "Product Deleted", "Deleted Product": product_id}

#----------------------------------------------------------------------
# Parameter with Type
#----------------------------------------------------------------------
@app.get("/product/{product_id}")
async def single_product(product_id:int):     # only int accepted
    return {"response":"Single Data Fetched", "product_id": product_id}

@app.get("/product/{product_title}")      # string accepted + int also act string
async def singlee_product(product_title:str):
    return {"response":"Single Data Fetched", "product_title": product_title}
----------------------------------------------------------------------
# Predefined values with enum 
----------------------------------------------------------------------
# Define an Enum class with allowed product categories
class ProductCategory(str, Enum):
    books = "books"
    clothing = "clothing"
    electronics = "electronics"

# Use the Enum as the type for the path parameter
@app.get("/product/{category}")
async def get_products(category:ProductCategory):
    return {"response": "Products fetched", "category": category}
------------------------------------------------------------------------
# Working with Python enumerations
------------------------------------------------------------------------
class ProductCategory(str, Enum):
    books = "books"
    clothing = "clothing"
    electronics = "electronics"
    other = "other"

@app.get("/product/{category}")
async def get_products(category:ProductCategory):
    if category == ProductCategory.books:
        return {"category": category, "message": "Books are awesome!"}
    elif category.value == "clothing":
        return {"category": category, "message": "Fashion trends here!"}
    elif category == ProductCategory.electronics.value:
        return {"category": category, "message": "Latest gadgets available!"}
    else:
        return {"category": category, "message": "Unknown category"}
