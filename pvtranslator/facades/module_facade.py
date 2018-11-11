from spyne import Unicode
from pvtranslator.entities.module import Module


class ModuleFacade:
    session = None

    def __init__(self,session):
        self.session = session

    def create_module(self, module: Module):
        self.session.add(module)
        self.session.commit()

    def delete_module(self, module: Module):
        self.session.delete(self.get_module_by_id(module.id))
        self.session.commit()

    def update_module(self, module: Module):
        persistent_module = self.get_module_by_id(module.id)
        persistent_module.name = module.name
        persistent_module.campaigns = module.campaigns
        self.session.commit()

    def get_module_by_name(self, name: Unicode):
        query = self.session.query(Module).filter_by(name=name)
        module_query = query.all()
        if len(module_query) == 0:
            return None
        else:
            return module_query[0]

    def get_module_by_id(self, module_id):
        query = self.session.query(Module).filter_by(id=module_id)
        module_query = query.all()
        if len(module_query) == 0:
            return None
        else:
            return module_query[0]
