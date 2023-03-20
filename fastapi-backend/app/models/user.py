from typing import List
from models.test import Test

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.sql import func
from models.base import Base


user_roles = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("role_id", ForeignKey("role.id"), primary_key=True),
)


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    role = Column(ENUM('ADMIN', 'TEACHER', 'STUDENT',
                  name='users_enum'), nullable=False)
    users: Mapped[List["User"]] = relationship(
        secondary=user_roles, back_populates="roles"
    )


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    fullname = Column(String)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, unique=True)
    roles: Mapped[List["Role"]] = relationship(
        secondary=user_roles, back_populates="users"
    )
    created_tests: Mapped[List["Test"]] = relationship(
        "Test", back_populates="creator")
