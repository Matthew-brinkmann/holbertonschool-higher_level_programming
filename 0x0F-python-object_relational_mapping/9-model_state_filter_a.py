#!/usr/bin/python3
'''
lists all State objects from the database hbtn_0e_6_usa that contain 'a'
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
    listOfFilteredStates = dbQueryObject.query(State)\
                                        .filter(State.name.contains('a'))\
                                        .order_by(State.id)
    for state in listOfFilteredStates:
        print(f'{state.id}: {state.name}')
    dbQueryObject.close()
