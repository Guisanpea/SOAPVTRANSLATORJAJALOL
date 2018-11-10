from sqlalchemy.orm import sessionmaker
from pvtranslator.entities.module import Module


class ModuleFacade:
    session = None

    def __init__(self,session):
        self.session = session

    def create_module(self, module: Module):
        self.session.add(module)
        self.session.commit()

    def delete_module(self, module: Module):
        self.session.delete(module)
        self.session.commit()

    def commit_module_update(self):
        self.session.commit()
