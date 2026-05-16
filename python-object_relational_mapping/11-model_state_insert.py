#!/usr/bin/python3
"""prints the first State object"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        )
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    count = session.query(State).count()
    new_state = State(count+1, "Louisiana")
    session.add(new_state)
    print(new_state.id)
    session.close()
