# build a schema using pydantic
from enum import Enum

from pydantic import BaseModel


class RoleEnum(str, Enum):
    admin = 'ADMIN'
    client = 'CLIENT'


class Role(BaseModel):
    role: RoleEnum

    class Config:
        orm_mode = True
