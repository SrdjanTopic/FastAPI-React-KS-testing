# build a schema using pydantic
from enum import Enum
from typing import List

from pydantic import BaseModel
from schemas.role import Role


class Gender(str, Enum):
    male = 'male'
    female = 'female'


class UserBase(BaseModel):
    fullname: str
    username: str
    email: str

    class Config:
        orm_mode = True


class UserRegister(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class UserGet(UserBase):
    roles: List[Role]

    class Config:
        orm_mode = True
