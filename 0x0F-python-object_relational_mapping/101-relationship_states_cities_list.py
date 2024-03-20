#!/usr/bin/python3
"""
A script that script that lists all State objects, and
corresponding City objects, contained in the database hbtn_0e_101_usa
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
    for state in session.query(State).order_by(State.id).all():
        print("{:d}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {:d}: {}".format(city.id, city.name))
    session.close()
