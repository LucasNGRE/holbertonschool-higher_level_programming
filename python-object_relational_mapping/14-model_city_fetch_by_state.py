#!/usr/bin/python3
"""
Prints all city objects from the database hbtn_0e_14_usa.
"""
import sys
from model_city import Base, City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>"
              .format(sys.argv[0]))
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).filter(
        City.state_id == State.id
    ).order_by(City.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
