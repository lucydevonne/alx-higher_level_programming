#!/usr/bin/python3
""" Adds the State object "Louisiana" to the database hbtn_0e_6_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """ Add the State object "Louisiana" to the database hbtn_0e_6_usa """

    # read mysql username, password and database name from arguments
    mysql_user = sys.argv[1]
    mysql_pwd = sys.argv[2]
    mysql_db = sys.argv[3]   

    # create a connection to the database
   engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(mysql_user, mysql_pwd, mysql_db),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    new = session.query(State.id).filter_by(State.name == 'Louisiana').first()
    
    print(new.id)
    session.close()
