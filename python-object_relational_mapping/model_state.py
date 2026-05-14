#!/usr/bin/python3
"""contains the class definition of a State"""
import sqlalchemy
import sqlalchemy.ext.declarative

Base = declarative_base()

class State(Base):
    """State class"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
