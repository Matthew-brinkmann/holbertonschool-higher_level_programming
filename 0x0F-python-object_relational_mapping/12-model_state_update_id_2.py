#!/usr/bin/python3
'''
changes the name of a State object from the database hbtn_0e_6_usa
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
    state = dbControlObject.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    dbControlObject.commit()
    dbControlObject.close()
