#!/usr/bin/python3
'''
creates the State “California” with the City “San Francisco”
'''
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    dbControlObject = Session()
    newState = State(name="California")
    newState.cities = [City(name="San Francisco")]
    dbControlObject.add(newState)
    dbControlObject.commit()
    dbControlObject.close()
