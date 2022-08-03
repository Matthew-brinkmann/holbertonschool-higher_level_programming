#!/usr/bin/python3
'''
deletes State objects from the database hbtn_0e_6_usa
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
    dbControlObject = Session()
    stateToDel = dbControlObject.query(State).filter(State.name.contains('a'))
    for state in stateToDel:
        dbControlObject.delete(state)
    dbControlObject.commit()
    dbControlObject.close()
