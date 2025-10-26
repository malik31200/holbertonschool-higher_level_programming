#!/usr/bin/python3
"""
model_city - a class definition of a city
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from model_state import Base, State


class City(Base):
    """
    City class that maps to the MySQL table 'cities'.
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State")
