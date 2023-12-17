#!/usr/bin/python3
"""model_state_filter_a module
Contains a script that shows all states that contains 'a' from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def first_state(db_useranme, db_password, db):
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
    states = session.query(State).order_by(State.id).filter(
        State.name.contains('a'))
    for state in states:
        print('{}: {}'.format(state.id, state.name))


if __name__ == '__main__':
    username, password, database = sys.argv[1:4]

    first_state(username, password, database)
