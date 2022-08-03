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
    # dbControlObject is a better name because it does more than
    # query it controls the DB object.
    dbControlObject = Session()
    newState = State(name='Louisiana')
    dbControlObject.add(newState)
    print(newState.id)
    dbControlObject.commit()
    dbControlObject.close()
