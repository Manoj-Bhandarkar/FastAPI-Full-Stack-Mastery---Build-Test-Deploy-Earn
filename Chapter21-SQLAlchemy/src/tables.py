from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String

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
# Address Table
#---------------
address = Table(
    "address",            # table name
    metadata,
    Column("id", Integer, primary_key=True),     # PK provide support for auto-increment
    Column("street", String, nullable=False, unique=True),
    Column("city", String, nullable=False, unique=True),
    Column("country", String, nullable=False, unique=True)
)
#--------------------------
# create table in Database
#--------------------------
def create_tables():
    metadata.create_all(engine) # find db path and in that db create table

#--------------------------
# drop table in Database
#--------------------------
def drop_tables():
    metadata.drop_all(engine) 