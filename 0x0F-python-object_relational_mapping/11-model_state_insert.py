#!/usr/bin/python3
""" 
    Adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    
    stateObj = State(name='Louisiana')
    session.add(stateObj)
    
    addedState = session.query(State).filter_by(name='Louisiana').first()
    print(addedState.id)
    session.commit()
