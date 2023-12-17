#!/usr/bin/python3
"""model_city_fetch_by_state module
Contains a script that prints all City objects from the database
"""
import sys
from model_state import Base
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def cities_by_state(db_user, db_pass, db_name):
    """cities_by_state function
    Fetch all the cities from the database by state
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
        print('{}: ({}) {}'.format(
            city.state.name, city.id, city.name
        ))


if __name__ == '__main__':
    user, password, db = sys.argv[1:4]

    cities_by_state(user, password, db)
