#!/usr/bin/python3
"""relation_cities_states_list module

Contains a script that lists all City objects from the db
"""
import sys
from relationship_city import City
from relationship_state import Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def list_cities(db_user, db_pass, db_name):
    """list_cities function
    Lists all City objects with their states
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        db_user, db_pass, db_name
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print('{}: {} -> {}'.format(
            city.id, city.name, city.state.name
        ))

    session.close()


if __name__ == '__main__':
    user, password, db = sys.argv[1:4]

    list_cities(user, password, db)
