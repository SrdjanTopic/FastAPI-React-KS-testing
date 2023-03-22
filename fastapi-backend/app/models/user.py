from typing import List

from models.base import Base
from models.manyToManyTables import (Learned_concepts, Test_submissions,
                                     User_roles)
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    fullname = Column(String)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    roles: Mapped[List["Role"]] = relationship(
        secondary=User_roles, back_populates="users"
    )
    learned_concepts: Mapped[List["Concept"]] = relationship(
        secondary=Learned_concepts, back_populates="learned_by_students"
    )
    created_tests = relationship(
        "Test", back_populates="creator")
    submitted_tests: Mapped[List["Test"]] = relationship(
        secondary=Test_submissions, back_populates="students"
    )
