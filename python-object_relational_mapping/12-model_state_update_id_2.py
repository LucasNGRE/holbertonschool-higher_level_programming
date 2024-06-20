#!/usr/bin/python3
"""
Changes the name of a State object
"""
import sys
from model_state import Base, State
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

    state = session.query(State).filter(
        State.id == 2
    ).first()
    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        print("Not found")

    session.close()
