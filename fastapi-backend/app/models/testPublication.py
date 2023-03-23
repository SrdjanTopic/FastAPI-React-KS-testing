from models._base import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Test_publication(Base):
    __tablename__ = 'test_publication'
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    is_published = Column(Boolean, default=False)
    test_id = Column(Integer, ForeignKey(
        "test.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    knowledge_space_id = Column(Integer, ForeignKey(
        "knowledge_space.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    test = relationship("Test", back_populates="publications")
    knowledge_space = relationship("Test", back_populates="test_publications")
