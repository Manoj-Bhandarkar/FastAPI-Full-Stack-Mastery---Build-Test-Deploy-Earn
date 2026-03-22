from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.config import create_tables, SessionDep
from app.product.services import create_product, get_all_products
from app.product.models import ProductCreate, ProductOut

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()  
    yield 

app = FastAPI(lifespan=lifespan)

