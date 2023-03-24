#!/usr/bin/env python3
"""Adds the State object Louisiana to the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check for correct usage
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} username password db_name")
        sys.exit(1)

    # Connect to the MySQL server
    username, password, db_name = sys.argv[1:]
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
                           pool_pre_ping=True)

    # Create the session and add the State object
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # Print the new states.id
    print(new_state.id)

