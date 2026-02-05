from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

metadata = MetaData()

#---------------
# User Table
#---------------
users = Table(
    "users",            # table name
    metadata,
    Column("id", Integer, primary_key=True),     # PK provide support for auto-increment
    Column("name", String(length=50), nullable=False),
    Column("email", String, unique=True)
)
#---------------
# Posts Table - One-To-Many
#---------------
posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("title", String, nullable=False),
    Column("content", String, nullable=False),
)
#--------------------------
## Profile Table - One-to-One
#--------------------------
profile = Table(
    "profile",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True),
    Column("title", String, nullable=False),
    Column("content", String, nullable=False),
)
#--------------------------
## addresses Table - Many to Many
#--------------------------
address = Table(
  "address",
  metadata,
  Column("id", Integer, primary_key=True),
  Column("street", String, nullable=False),
  Column("country", String, nullable=False),
)
#--------------------------
## Association between user and address - Extra Table 
#--------------------------
user_address_association = Table(
  "user_address_association",
  metadata,
  Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
  Column("address_id", Integer, ForeignKey("address.id", ondelete="CASCADE"), primary_key=True),
)

#--------------------------
# create table in Database
#--------------------------
def create_tables():
    metadata.create_all(engine) # find db path and in that db create table
