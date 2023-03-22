from typing import List

from models.base import Base
from models.manyToManyTables import Test_submissions
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.sql import func


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    name = Column(String, nullable=False)
    creator_id = Column(Integer, ForeignKey("user.id"))
    creator = relationship(
        "user", back_populates="created_tests")
    questions = relationship(
        "Question", back_populates="test")
    students: Mapped[List["User"]] = relationship(
        secondary=Test_submissions, back_populates="submitted_tests"
    )
