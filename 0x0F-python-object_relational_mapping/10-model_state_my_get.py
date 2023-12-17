#!/usr/bin/python3
"""model_state_my_get module
Contains a script that prints the id of the searched State from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def search_state(db_useranme, db_password, db, search):
    """search a state
    A function that prints the id of the searched state
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
    state = session.query(State).order_by(State.id).filter(
        State.name == search).first()
    if (state is not None):
        print(state.id)
    else:
        print('Not found')


if __name__ == '__main__':
    username, password, database, search = sys.argv[1:5]

    search_state(username, password, database, search)
