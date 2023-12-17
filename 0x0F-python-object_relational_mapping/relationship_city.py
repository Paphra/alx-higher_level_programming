#!/usr/bin/python3
"""model_city module
Contains the City model
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """City model
    The model class for the City
    """

    __tablename__ = 'cities'
    id = Column(
        Integer, nullable=False, primary_key=True,
        autoincrement='auto')
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship('State', back_populates='cities')
