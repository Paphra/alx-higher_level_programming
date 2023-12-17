#!/usr/bin/python3
"""model_state_insert module
Contains a script that inserts a new state the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def insert_state(db_useranme, db_password, db):
    """insert_state function
    A function that inserts a new State "Louisiana"
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
    new_state = State()
    new_state.name = 'Louisiana'
    session.add(new_state)
    session.commit()
    print(new_state.id)


if __name__ == '__main__':
    username, password, database = sys.argv[1:4]

    insert_state(username, password, database)
