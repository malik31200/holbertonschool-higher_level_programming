#!/usr/bin/python3
"""
Print the id of the State object that matches the name
passed as
argument from the database hbtn_0e_6_usa.
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

    result = session.query(State).filter_by(name=argv[4]).first()

    if result:
        print(result.id)
    else:
        print("Not found")

    session.close()
