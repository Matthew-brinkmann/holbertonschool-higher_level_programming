#!/usr/bin/python3
'''
lists all State objects from the database hbtn_0e_6_usa,
names passed as argument
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
    stateNameSearch = argv[4]
    stateSearch = dbQueryObject.query(State)\
                         .filter(State.name == stateNameSearch)\
                         .first()
    if stateSearch is not None:
        print(f"{stateSearch.id}")
    else:
        print("Not found")
    dbQueryObject.close()
