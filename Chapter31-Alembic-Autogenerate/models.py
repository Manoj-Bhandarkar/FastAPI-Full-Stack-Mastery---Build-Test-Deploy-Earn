from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer
from db import engine

class Base(DeclarativeBase):
  pass

# User Model
class User(Base):
  __tablename__ = "users"

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False)
  email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
  phone: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
  address: Mapped[str] = mapped_column(String, nullable=False)
  def __repr__(self) -> str:
    return f"<User(id={self.id}, name={self.name}, email={self.email})>"


## use command 
# alembic revision --autogenerate -m "create users table"
# alembic upgrade head

#Add new field after table created
# class User(Base):
#   ...
#   ...
#   address: Mapped[str] = mapped_column(String, nullable=False)

# alembic revision –autogenerate –m “add address column”
# alembic upgrade head