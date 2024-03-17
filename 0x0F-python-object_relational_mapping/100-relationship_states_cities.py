#!/usr/bin/python3
"""creates the State “California” with the City “San Francisco”
from the database
"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    CA = State(name="California", cities=[City(name="San Francisco")])
    session.add(CA)
    session.commit()
    session.close()
