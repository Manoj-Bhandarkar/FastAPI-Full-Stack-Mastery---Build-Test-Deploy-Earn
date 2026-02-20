from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from src.user import models
from src.product import models