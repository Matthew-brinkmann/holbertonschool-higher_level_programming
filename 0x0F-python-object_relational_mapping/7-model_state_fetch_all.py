#!/usr/bin/python3
'''
script that lists all State objects from the database hbtn_0e_6_usa
'''
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    dbQueryObject = Session()
    listOfAllStates = dbQueryObject.query(State).order_by(State.id)
    for state in listOfAllStates:
        print(f'{state.id}: {state.name}')
    dbQueryObject.close()
