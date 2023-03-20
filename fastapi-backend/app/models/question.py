from typing import List
from models.answer import Answer
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.sql import func
from models.base import Base


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    question = Column(String, nullable=False)
    points = Column(Integer, default=5, nullable=False)
    test_id = Column(Integer, ForeignKey("test.id"))
    test = relationship(
        "test", back_populates="questions")
    answers: Mapped[List["Answer"]] = relationship(
        "Answer", back_populates="question")
