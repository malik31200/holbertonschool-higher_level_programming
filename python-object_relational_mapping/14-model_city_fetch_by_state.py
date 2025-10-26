#!/usr/bin/python3
"""
Script that prints all City objects
from the database hbtn_0e_14_usa.
"""
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1],
            argv[2],
            argv[3]
        ),
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id.asc()).all()

    for city in cities:
        print(f"{city.state.name}: {city.id} {city.name}")

    session.close()
