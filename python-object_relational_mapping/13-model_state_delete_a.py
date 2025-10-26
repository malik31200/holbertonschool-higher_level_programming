#!/usr/bin/python3
"""
Script that deletes all State objects
with a name containing the letter a.
"""
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session, sessionmaker

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

    states = session.query(State).filter(State.name.like("%a%")).all()
    for state in states:
        session.delete(state)

    session.commit()

    session.close()
