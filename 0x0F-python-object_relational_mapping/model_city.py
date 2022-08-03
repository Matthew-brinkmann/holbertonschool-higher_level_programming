#!/usr/bin/python3
'''
Module contains declarative_base and city Class.
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    '''
    class City that inherits from Base class:
        Defined as TableName = cities:
        id (primary Key, int)
        name (string, not NULL)
        state_id (integer, not NULL, foreign key to states.id)
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
