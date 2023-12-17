#!/usr/bin/python3
"""relation_states_cities module
Contains a script that creates the states
- California with City San Francisco
"""
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def create_state_with_city(db_user, db_pass, db_name):
    """create_state_with_city function
    Creates a State with a City
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        db_user, db_pass, db_name
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    state = State(name='California')
    city = City(name='San Francisco')
    state.cities = [city]
    session.add(state)
    session.commit()


if __name__ == '__main__':
    user, password, db = sys.argv[1:4]

    create_state_with_city(user, password, db)
