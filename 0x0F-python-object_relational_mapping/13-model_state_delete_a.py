#!/usr/bin/python3
"""model_state_delete_a module
Contains a script that deletes the States which have the name with a
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def delete_all_a_states(db_user, db_pass, db_name):
    """delete_all_a_states function
    Deletes all the states with the name that has a
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        db_user, db_pass, db_name
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.contains('a')).all()
    for state in states:
        session.delete(state)
    session.commit()


if __name__ == '__main__':
    user, password, db = sys.argv[1:4]

    delete_all_a_states(user, password, db)
