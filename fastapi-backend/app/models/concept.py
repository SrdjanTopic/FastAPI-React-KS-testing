from typing import List

from models._base import Base
from models.manyToManyTables import Learned_concepts
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.sql import func


class Concept(Base):
    __tablename__ = 'concept'
    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    concept = Column(String, nullable=False)
    questions = relationship(
        "Concept", back_populates="concept")
    profession_id = Column(Integer, ForeignKey(
        "profession.id", onupdate="CASCADE"))
    profession = relationship(
        "profession", back_populates="required_concepts")
    learned_by_students: Mapped[List["User"]] = relationship(
        secondary=Learned_concepts, back_populates="learned_concepts"
    )
    sources: Mapped[List["Concept"]] = relationship(
        secondary=Learned_concepts, back_populates="destinations"
    )
    destinations: Mapped[List["Concept"]] = relationship(
        secondary=Learned_concepts, back_populates="sources"
    )
