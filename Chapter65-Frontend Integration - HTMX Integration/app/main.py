from fastapi import FastAPI, Request, Form
from contextlib import asynccontextmanager
from app.db.config import create_tables, SessionDep
from app.product.services import create_product, get_all_products
from app.product.models import ProductCreate, ProductOut

from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()  
    yield 

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
template = Jinja2Templates(directory="app/templates")
