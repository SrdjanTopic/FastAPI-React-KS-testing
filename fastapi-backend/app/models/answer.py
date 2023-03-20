from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.base import Base


class Answer(Base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    answer = Column(String, nullable=False)
    isCorrect = Column(Boolean, default=False, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship(
        "question", back_populates="answers")