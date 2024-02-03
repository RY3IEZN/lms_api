from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


users = ["uneku"]


class User(BaseModel):
    email: str
    is_active: bool


# get list of users
@app.get("/users")
async def get_users():
    return users


# create a new user
@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": "Succesfully added user"}
