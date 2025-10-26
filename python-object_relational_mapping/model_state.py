#!/usr/bin/python3
"""
model_state - a class definition of a state
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that maps to the MySQL table 'states'.
    """
    __tablename__ = "States"
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
