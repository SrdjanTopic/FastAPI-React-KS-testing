from typing import List
from models.concept import Concept
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.sql import func
from models.base import Base


class Profession(Base):
    __tablename__ = 'profession'
    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    profession = Column(String, nullable=False)
    required_concepts = relationship(
        "Profession", back_populates="profession")
