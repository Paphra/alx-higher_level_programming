#!/usr/bin/python3
"""relationship_states_cities_list module

Contains a script to list all State objects
and corresponding City objects in the database
"""

import sys
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def list_states_with_cities(db_user, db_pass, db_name):
    """list_states_with_cities function
    Lists all the State Objects with their corresponding citites
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        db_user, db_pass, db_name
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    states = session.query(
        State).order_by(
            State.id).join(City).order_by(City.id).all()

    for state in states:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))


if __name__ == '__main__':
    user, password, db = sys.argv[1:4]

    list_states_with_cities(user, password, db)
