from typing import Annotated
from fastapi import FastAPI, Header, Body
from pydantic import BaseModel, Field
app = FastAPI()

#-----------------------------
## Header Parameters
#-----------------------------
@app.get("/products")
async def get_products(user_agent: Annotated[str|None, Header()] = None):
  return user_agent

# curl -H "User-Agent: Mozilla/5.0" http://127.0.0.1:8000/products

#-----------------------------
## Handling Duplicate Headers
#-----------------------------
@app.get("/products1")
async def get_product(x_product_token: Annotated[list[str] | None, Header()] = None):
    return {
        "x_product_token": x_product_token or []
    }

# curl -H "X-Product-Token: token1" -H "X-Product-Token: token2" http://127.0.0.1:8000/products

#------------------------------------
## Headers with a Pydantic Model
#------------------------------------
class Product_Header_Pydantic(BaseModel):
  #model_config = {"extra":"forbid"}         # extra forbid
  authorization: str
  accept_language: str | None = None
  x_tracking_id: list[str] = []

@app.get("/products2")
async def get_product_header_pydantic(headers: Annotated[Product_Header_Pydantic, Header()]):
    return {
        "headers": headers
    }
# curl -H "Authorization: Bearer token123" -H "Accept-Language: en-US" -H "X-Tracking-Id: track1" -H "X-Tracking-Id: track2" http://127.0.0.1:8000/products
