from fastapi import FastAPI

app = FastAPI()

# Single Query Parameter
@app.get("/product")
async def product(category:str):
  return {"status":"OK", "category":category}

# # Multiple Query Parameter
@app.get("/product")
async def product_multi_query_param(category:str, limit:int):
  return {"status":"OK", "category":category, "limit":limit}

# # Default Query Parameter
@app.get("/product")
async def product_default_query_param(category:str, limit:int=10):
  return {"status":"OK", "category":category, "limit":limit}

# # Optional Query Parameter
@app.get("/product")
async def product_optional_query_param(limit:int, category:str | None = None):
  return {"status":"OK", "category":category, "limit":limit}

#Path and Query parameter
@app.get("/product/{year}")
async def product_path_query_param(year:str, category:str):
  return {"status":"OK", "year":year, "category":category}