from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pvtranslator import tableModel
from pvtranslator.entities import get_entities_import
from wsgiref.simple_server import make_server
from spyne.server.wsgi import WsgiApplication


def start_engine():
    get_entities_import()
    engine = create_engine('mysql+mysqlconnector://iweb:iweb@192.168.99.100/iweb')
    tableModel.TableModel.Attributes.sqla_metadata.create_all()
    return sessionmaker(bind=engine)


def start_application():
    from pvtranslator.services import get_application
    wsgi_app = WsgiApplication(get_application())
    server = make_server('127.0.0.1', 8050, wsgi_app)
    print("server started")
    server.serve_forever()


if __name__ == "__main__":
    start_engine()
    start_application()

