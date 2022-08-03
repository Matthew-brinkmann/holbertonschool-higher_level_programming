#!/usr/bin/python3
'''
Module contains declarative_base and State Class.
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    class state that inherits from Base class:
        Defined as TableName = States:
        id (primary Key, int)
        name (string, not NULL)
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
