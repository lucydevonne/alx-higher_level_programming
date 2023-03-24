#!/usr/bin/python3

"""
Deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
   takes arguments: mysql-username, mysql-password, database-name
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine =\
        create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(
            State.name.ilike('%a%')).order_by(State.id):
        session.delete(state)
    session.commit()
