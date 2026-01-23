from fastapi import FastAPI

app = FastAPI()


@app.get("/product")
async def all_products():
    return {"response": "All products"}


@app.get("/product/{product_id}")
async def single_products(product_id: int):
    return {"response": "Single products", "product_id": product_id}


@app.post("/product")
async def create_products(new_product: dict):
    return {"response": "Product Created", "new product": new_product}

@app.put("/product/{product_id}")
async def update_products(new_updated_product: dict, product_id: int):
    return {"response": "Complete Product Updated", "product_id":product_id, "new updated product": new_updated_product}


@app.patch("/product/{product_id}")
async def partial_update_products(new_updated_product: dict, product_id: int):
    return {"response": "Partial Product Updated", "product_id":product_id, "new updated product": new_updated_product}

@app.delete("/product/{product_id}")
async def delete_products(product_id: int):
    return {"response": "Product Deleted", "Deleted Product": product_id}
