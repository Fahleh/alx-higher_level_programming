#!/usr/bin/python3
"""
    Contains the State class and a Base instance of declarative_base().
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Inherits from Base (imported from model_state)
    links to the MySQL table cities

    Class attribute id that represents a column of
    an auto-generated, unique integer, can't be null and is a primary key

    Class attribute name that represents a column
    of a string with max 128 characters and can't be null
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
