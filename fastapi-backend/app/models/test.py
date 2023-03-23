from typing import List

from models._base import Base
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
    creator_id = Column(Integer, ForeignKey(
        "user.id", onupdate="CASCADE", ondelete="CASCADE"))
    creator = relationship(
        "User", back_populates="created_tests")
    questions = relationship(
        "Question", back_populates="test")
    students: Mapped[List["User"]] = relationship(
        secondary=Test_submissions, back_populates="submitted_tests"
    )
    knowledge_spaces = relationship(
        "Knowledge_space", back_populates="test")
    publications = relationship(
        "Knowledge_space", back_populates="test")
