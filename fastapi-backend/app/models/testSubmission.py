# from typing import List

# from models.manyToManyTables import Submitted_answers
# from models.base import Base
# from sqlalchemy import Column, DateTime, ForeignKey, Integer
# from sqlalchemy.orm import relationship, Mapped
# from sqlalchemy.sql import func


# class Test_submission(Base):
#     __tablename__ = 'test_submission'
#     id = Column(Integer, primary_key=True)
#     time_created = Column(DateTime(timezone=True), server_default=func.now())
#     time_updated = Column(DateTime(timezone=True), onupdate=func.now())
#     test_id = Column(Integer, ForeignKey("test.id"))
#     test = relationship(
#         "test", back_populates="submissions")
#     student_id = Column(Integer, ForeignKey("user.id"))
#     student = relationship(
#         "user", back_populates="submitted_tests")
#     answers: Mapped[List["Answer"]] = relationship(
#         secondary=Submitted_answers, back_populates="test_submissions"
#     )
