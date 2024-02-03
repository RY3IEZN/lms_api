from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title="Fast Api for lms",
    description="LMS Api for managing students and course",
    version="0.0.1",
    contact={
        "name": "Uneku",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


# entry point
@app.get("/")
async def root():
    return {"message": "welcome to the backend"}


# get list of users
@app.get("/users", response_model=List[User])
async def get_users():
    return users


# create a new user
@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": "Succesfully added user"}


# get user by id
@app.get("/users/{id}")
async def get_user(
    id: int = Path(
        ...,
        description="the Id of the user",
    ),
    q: str = Query(None, max_length=5),
):
    return {"user": users[id], "query": q}
