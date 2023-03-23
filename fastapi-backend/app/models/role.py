from typing import List

from models._base import Base
from models.manyToManyTables import User_roles
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import Mapped, relationship


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    role = Column(ENUM('ADMIN', 'TEACHER', 'STUDENT',
                  name='users_enum'), nullable=False)
    users: Mapped[List["User"]] = relationship(
        secondary=User_roles, back_populates="roles"
    )
