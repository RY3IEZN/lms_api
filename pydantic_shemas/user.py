from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class UserBase(BaseModel):
    email: str
    role: int


class UserCreate(UserBase): ...


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
