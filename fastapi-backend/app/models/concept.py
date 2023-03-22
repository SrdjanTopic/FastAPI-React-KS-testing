from typing import List
from models.question import Question
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.sql import func
from models.base import Base


class Concept(Base):
    __tablename__ = 'concept'
    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    concept = Column(String, nullable=False)
    questions = relationship(
        "Concept", back_populates="concept")
    profession_id = Column(Integer, ForeignKey("profession.id"))
    profession = relationship(
        "profession", back_populates="required_concepts")
