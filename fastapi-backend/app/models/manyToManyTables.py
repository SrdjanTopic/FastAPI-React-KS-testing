from typing import List

from models._base import Base
from sqlalchemy import (Column, DateTime, ForeignKey, ForeignKeyConstraint,
                        Integer, func)
from sqlalchemy.orm import Mapped, relationship


class User_roles (Base):
    __tablename__ = 'user_roles'
    user_id = Column(Integer, ForeignKey(
        'user.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    role_id = Column(Integer, ForeignKey(
        'role.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)


class Learned_concepts (Base):
    __tablename__ = 'learned_concepts'
    student_id = Column(Integer, ForeignKey(
        'user.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    concept_id = Column(Integer, ForeignKey(
        'concept.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)


class Submitted_answers (Base):
    __tablename__ = 'submitted_answers'
    test_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, primary_key=True)
    answer_id = Column(Integer, ForeignKey(
        'answer.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)

    __table_args__ = (
        ForeignKeyConstraint(
            ['test_id', 'student_id'],
            ['test_submissions.test_id', 'test_submissions.student_id'], ondelete="CASCADE", onupdate="CASCADE"
        ),
    )


class Test_submissions(Base):
    __tablename__ = 'test_submissions'
    test_id = Column(Integer, ForeignKey("test.id", ondelete="CASCADE", onupdate="CASCADE"),
                     primary_key=True)
    student_id = Column(Integer, ForeignKey(
        "user.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    answers: Mapped[List["Answer"]] = relationship(
        secondary=Submitted_answers, back_populates="test_submissions"
    )


class Concept_relations(Base):
    __tablename__ = 'concept_relations'
    source_id = Column(Integer, ForeignKey("concept.id", ondelete="CASCADE", onupdate="CASCADE"),
                       primary_key=True)
    destination_id = Column(Integer, ForeignKey("concept.id", ondelete="CASCADE", onupdate="CASCADE"),
                            primary_key=True)
    knowledge_space_id = Column(Integer, ForeignKey("knowledge_space.id", ondelete="CASCADE", onupdate="CASCADE"),
                                primary_key=True)
