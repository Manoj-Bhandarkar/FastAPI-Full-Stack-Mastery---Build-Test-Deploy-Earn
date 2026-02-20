from fastapi import FastAPI
from src.user import services as user_services
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name : str
    email : str

@app.post("/user")
def create_user(user:UserCreate):
    user_services.create_user(name=user.name, email=user.email)
    return {"status":"user created"}

@app.get("/users")
def all_users():
    users = user_services.get_all_users()
    return users

