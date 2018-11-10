from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pvtranslator import base


def start_engine():
    # we need to import models in order to create correct database
    import pvtranslator.entities
    engine = create_engine('mysql+mysqlconnector://iweb:iweb@192.168.99.100/iweb')
    base.Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)


if __name__ == "__main__":
    start_engine()
