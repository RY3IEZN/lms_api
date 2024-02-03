from pydantic import BaseModel
from typing import Optional, List
import fastapi

router = fastapi.APIRouter()


users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


# get list of users
@router.get("/users", response_model=List[User])
async def get_users():
    return users


# create a new user
@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": "Succesfully added user"}


# get user by id
@router.get("/users/{id}")
async def get_user():
    return {"user": users[id]}
