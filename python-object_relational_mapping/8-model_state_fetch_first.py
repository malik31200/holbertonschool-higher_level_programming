#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
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

    first_state = session.query(State).filter_by(id=1).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")

    session.close()
