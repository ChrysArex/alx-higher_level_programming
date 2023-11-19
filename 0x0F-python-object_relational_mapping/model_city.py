#!/usr/bin/python3
"""
python file that contains the class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """Map the table states with the state class"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
