from models.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, ForeignKeyConstraint, Integer, func
from sqlalchemy.orm import Mapped, relationship
from typing import List


class User_roles (Base):
    __tablename__ = 'user_roles'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)


class Submitted_answers (Base):
    __tablename__ = 'submitted_answers'
    test_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, primary_key=True)
    answer_id = Column(Integer, ForeignKey('answer.id'), primary_key=True)

    __table_args__ = (
        ForeignKeyConstraint(
            ['test_id', 'student_id'],
            ['test_submissions.test_id', 'test_submissions.student_id']
        ),
    )


class Test_submissions(Base):
    __tablename__ = 'test_submissions'
    test_id = Column(Integer, ForeignKey("test.id"), primary_key=True)
    student_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    answers: Mapped[List["Answer"]] = relationship(
        secondary=Submitted_answers, back_populates="test_submissions"
    )
