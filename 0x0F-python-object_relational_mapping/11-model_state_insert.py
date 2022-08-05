#!/usr/bin/python3
'''
inserts a State object to the database hbtn_0e_6_usa
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
    new_state = State(name='Louisiana')
    dbControlObject.add(new_state)
    dbControlObject.commit()
    dbControlObject.flush()
    print(new_state.id)
    dbControlObject.close()
