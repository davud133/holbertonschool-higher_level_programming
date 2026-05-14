#!/usr/bin/python3
"""contains the class definition of a State"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State class"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
