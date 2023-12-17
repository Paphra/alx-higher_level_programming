#!/usr/bin/python3
"""model_state_fetch_first module
Contains a script that shows the first State object from the database
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
    for state in session.query(State).order_by(State.id).limit(1):
        print('{}: {}'.format(state.id, state.name))
    if (session.query(State).count()  == 0):
        print('Nothing')


if __name__ == '__main__':
    username, password, database = sys.argv[1:4]

    list_all_states(username, password, database)
