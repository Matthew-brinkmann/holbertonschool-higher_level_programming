#!/usr/bin/python3
'''
ists all State objects, and corresponding City objects
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
    fullListOfStateAndCity = dbControlObject.query(City).all()
    for city in fullListOfStateAndCity:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    dbControlObject.close()
