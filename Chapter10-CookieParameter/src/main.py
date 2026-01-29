from fastapi import FastAPI, Cookie, Body
from typing import Annotated
from pydantic import BaseModel, Field
app = FastAPI()

#--------------------------------------
## Cookie Parameters
#--------------------------------------
@app.get("/products/recommendations")
async def get_recommendation(session_id: Annotated[str | None, Cookie()] = None):
  if session_id:
    return {"message": f"Recommendations for session {session_id}", "session_id": session_id}
  return {"message": "No session ID provided, showing default recommendations"}

# curl -H "Cookie: session_id=abc123" http://127.0.0.1:8000/products/recommendations => {"message": f"Recommendations for session abc123", "session_id": abc123}
# curl -H  http://127.0.0.1:8000/products/recommendations   => {"message": "No session ID provided, showing default recommendations"}
#===================================================================================================

#--------------------------------------
# ## Cookies with a Pydantic Model
#--------------------------------------
class Product_Cookies_Pydantic(BaseModel):
  session_id: str
  preferred_category: str | None = None
  tracking_id: str | None = None

@app.get("/products/getrecommendations-pydantic")
async def get_recommendation_pydantic(cookies: Annotated[Product_Cookies_Pydantic, Cookie()]):
  response = {"session_id": cookies.session_id}
  if cookies.preferred_category:
    response["message"] = f"Recommendations for {cookies.preferred_category} products"
  else:
    response["message"] = f"Default recommendations for session {cookies.session_id}"
  if cookies.tracking_id:
      response["tracking_id"] = cookies.tracking_id
  return response

# curl -H "Cookie: session_id=abc123; preferred_category=Electronics; tracking_id=xyz789" http://127.0.0.1:8000/products/recommendations-pydantic

#--------------------------------------
## Forbidding Extra Cookies
#--------------------------------------
class Product_Cookies_Forbid_Extra(BaseModel):
  model_config = {"extra": "forbid"}
  session_id: str
  preferred_category: str | None = None
  tracking_id: str | None = None

@app.get("/products/recommendation-forbid")
async def get_recommendation_forbit_extra(cookies: Annotated[Product_Cookies_Forbid_Extra, Cookie()]):
  response = {"session_id": cookies.session_id}
  if cookies.preferred_category:
    response["message"] = f"Recommendations for {cookies.preferred_category} products"
  else:
    response["message"] = f"Default recommendations for session {cookies.session_id}"
  if cookies.tracking_id:
      response["tracking_id"] = cookies.tracking_id
  return response

#--------------------------------------
# Combining Cookie with Body Parameters
#--------------------------------------
class Product_Cookies(BaseModel):
  model_config = {"extra": "forbid"}
  session_id: str = Field(title="Session ID", description="User session identifier")
  preferred_category: str | None = Field(default=None, title="Preferred Category", description="User's preferred product category")

class Price_Filter_Body(BaseModel):
    min_price: float = Field(ge=0, title="Minimum Price", description="Minimum price for recommendations")
    max_price: float | None = Field(default=None, title="Maximum Price", description="Maximum price for recommendations")

@app.post("/products/recommendations-cookie-body")
async def get_recommendation_cookie_body(
   cookies: Annotated[Product_Cookies, Cookie()],
   price_filter: Annotated[Price_Filter_Body, Body(embed=True)]
   ):
  response = {"session_id": cookies.session_id}
  if cookies.preferred_category:
    response["category"] = cookies.preferred_category
  response["price_range"] = {
        "min_price": price_filter.min_price,
        "max_price": price_filter.max_price
    }
  response["message"] = f"Recommendations for session {cookies.session_id} with price range {price_filter.min_price} to {price_filter.max_price or 'unlimited'}"
  return response

# curl -X POST -H "Cookie: session_id=abc123; preferred_category=Electronics" -H "Content-Type: application/json" -d "{\"price_filter\":{\"min_price\":50.0,\"max_price\":1000.0}}" http://127.0.0.1:8000/products/recommendations-cookie-body
