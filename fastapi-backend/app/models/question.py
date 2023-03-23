from models._base import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    question = Column(String, nullable=False)
    points = Column(Integer, default=5, nullable=False)
    test_id = Column(Integer, ForeignKey(
        "test.id", ondelete="CASCADE", onupdate="CASCADE"))
    test = relationship(
        "test", back_populates="questions")
    answers = relationship(
        "Answer", back_populates="question")
    concept_id = Column(Integer, ForeignKey("concept.id", onupdate="CASCADE"))
    concept = relationship(
        "concept", back_populates="questions")
