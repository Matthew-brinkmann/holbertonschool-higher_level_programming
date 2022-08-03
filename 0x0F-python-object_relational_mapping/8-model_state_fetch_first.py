#!/usr/bin/python3
'''
script that lists the first State objects from the database hbtn_0e_6_usa
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
    firstState = dbQueryObject.query(State).order_by(State.id).first()
    if (firstState is not None):
        print(f'{firstState.id}: {firstState.name}')
    else:
        print('Nothing')
    dbQueryObject.close()