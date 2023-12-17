#!/usr/bin/python3
"""mode_state_update_id_2 module

Contains a script to update the State object from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def update_state(db_username, db_password, db_name):
    """update_state function
    Updates the State with id = 2 to New Mexico
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        db_username, db_password, db_name
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == 2).first()
    if (state is not None):
        state.name = 'New Mexico'
    session.commit()


if __name__ == '__main__':
    user, password, db = sys.argv[1:4]

    update_state(user, password, db)
