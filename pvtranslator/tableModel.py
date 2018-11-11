from spyne.model.complex import TTableModel
from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+mysqlconnector://iweb:iweb@192.168.99.100/iweb')
TableModel = TTableModel(MetaData(bind=engine))