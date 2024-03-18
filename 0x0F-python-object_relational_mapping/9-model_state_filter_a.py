#!/usr/bin/python3
""" 
    Lists all states from the database hbtn_0e_6_usa filtered by
    those containing the letter 'a'.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    sessionMaker = sessionmaker(bind=engine)
    session = sessionMaker()
    for state in session.query(State).filter(State.name.like('%a%')):
        print(state.id, state.name, sep=": ")
