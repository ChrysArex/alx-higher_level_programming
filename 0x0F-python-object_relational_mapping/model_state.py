#!/usr/bin/python3
"""
python file that contains the class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Map the table states with the state class"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
