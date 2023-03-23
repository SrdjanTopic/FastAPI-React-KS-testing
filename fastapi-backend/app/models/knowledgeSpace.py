from models._base import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Knowledge_space(Base):
    __tablename__ = 'knowledge_space'
    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    is_generated = Column(Boolean, default=False)
    relations = relationship(
        "Concept_relations", back_populates="knowledge_space")
    test_id = Column(Integer, ForeignKey(
        "test.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=True)
    test = relationship("Test", back_populates="knowledge_spaces")
    publications = relationship(
        "Knowledge_space", back_populates="knowledge_space")
