#!/usr/bin/python3
"""model_state module
Contains the class definition of a State and and instance of
Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State model class

    Defines the model for the State abstraction
    """

    __tablename__ = 'states'
    id = Column(
        Integer, primary_key=True, autoincrement='auto',
        nullable=False)
    name = Column(String(128), nullable=False)
