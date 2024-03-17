#!/usr/bin/python3
"""A script that deletes all State objects with a name containing the
letter a from the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit()

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id).order_by(City.id)

    for city in cities:
        print("{:s}: ({:d}) {:s}".format(city[0], city[1], city[2]))

    session.close()
