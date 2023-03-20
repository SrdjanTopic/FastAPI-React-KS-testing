from typing import List
from models.question import Question
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.sql import func
from models.base import Base


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    name = Column(String, nullable=False)
    creator_id = Column(Integer, ForeignKey("user.id"))
    creator = relationship(
        "user", back_populates="created_tests")
    questions: Mapped[List["Question"]] = relationship(
        "Question", back_populates="test")
