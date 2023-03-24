#!/usr/bin/python3
""" Adds the State object "Louisiana" to the database hbtn_0e_6_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """ Add the State object "Louisiana" to the database hbtn_0e_6_usa """

    # read mysql username, password and database name from arguments
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])    

    # create a connection to the database
    engine = create_engine(db_url)

    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # create a new State object
    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    
    print(louisiana.id)
    session.close()
