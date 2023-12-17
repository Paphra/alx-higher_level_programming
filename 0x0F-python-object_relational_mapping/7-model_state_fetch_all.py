#!/usr/bin/python3
"""model_state_fetch_all module
Contains a script that lists all State objects from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def list_all_states(db_useranme, db_password, db):
    """List all users
    A function that prints all States
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            db_useranme, db_password, db
        ), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        print('{}: {}'.format(state.id, state.name))


if __name__ == '__main__':
    username, password, database = sys.argv[1:4]

    list_all_states(username, password, database)
