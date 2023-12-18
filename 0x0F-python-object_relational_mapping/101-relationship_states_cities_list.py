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

    results = session.query(
        State, City).filter(State.id == City.state_id).order_by(
            State.id, City.id).all()
    current_id = None
    for state, city in results:
        if state.id != current_id:
            print('{}: {}'.format(state.id, state.name))
            current_id = state.id
        print('    {}: {}'.format(city.id, city.name))
    session.close()


if __name__ == '__main__':
    user, password, db = sys.argv[1:4]

    list_states_with_cities(user, password, db)
