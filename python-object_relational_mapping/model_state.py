#!/usr/bin/python3
"""contains the class definition of a State"""

if __name__ == "__main__":
    import sqlalchemy
    import sqlalchemy.ext.declerative

    Base = declerative_base()

    class State(Base):
        __tablename__ = "states"

        id = column(Integer, primary_key=True)
        name = column(String(128), nullable=False)
