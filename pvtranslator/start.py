from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pvtranslator import base


def start_engine():
    engine = create_engine('mysql+mysqlconnector://iweb:iweb@localhost/iweb')
    base.Base.metadata.create_all(engine)
    sessionmaker(bind=engine)


if __name__ == "__main__":
    start_engine()
