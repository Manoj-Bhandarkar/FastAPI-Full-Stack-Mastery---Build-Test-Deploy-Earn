from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any, Optional

app = FastAPI()

## Excluding Unset Default Values

products_db = {
    "1": {"id": "1", "name": "Laptop", "price": 999.99, "stock": 10, "is_active": True},
    "2": {"id": "2", "name": "Smartphone", "price": 499.99, "stock": 50, "is_active": False}
}

class Product(BaseModel):
    id: str
    name: str
    price: float
    description: Optional[str] = None
    tax: float = 15.0  # Default tax rate

@app.get("/products1/{product_id}", response_model=Product, response_model_exclude_unset=True)
async def get_product1(product_id: str):
    return products_db.get(product_id, {})

## Including Specific Fields
@app.get("/products2/{product_id}", response_model=Product, response_model_include={"name", "price"})
async def get_product2(product_id: str):
    return products_db.get(product_id, {})

## Excluding Specific Fields
@app.get("/products3/{product_id}", response_model=Product, response_model_exclude={"tax", "description"})
async def get_product3(product_id: str):
    return products_db.get(product_id, {})