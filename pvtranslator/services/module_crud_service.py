from spyne import ServiceBase, rpc, Integer, UnsignedInteger32, Iterable
from pvtranslator.facades.module_facade import ModuleFacade
from pvtranslator.start import start_engine
from pvtranslator.entities.module import Module


class ModuleCrudService(ServiceBase):

    # create module if it's possible and return id
    @rpc(Module, _returns=UnsignedInteger32)
    def create_module(ctx, module):
        module_id = -1

        if module.id is None:
            scoped_session = start_engine()
            session = scoped_session()
            facade = ModuleFacade(session)
            facade.create_module(module=module)
            module_id = facade.get_module_by_name(name=module.name).id

        session.close()
        return module_id

    # delete module in cascade
    @rpc(Module)
    def delete_module(ctx, module):
        scoped_session = start_engine()
        session = scoped_session()
        facade = ModuleFacade(session)
        facade.delete_module(module=module)
        session.close()

    # update module
    @rpc(Module)
    def update_module(ctx, module):
        scoped_session = start_engine()
        session = scoped_session()
        facade = ModuleFacade(session)
        facade.update_module(module=module)
        session.close()

    # return module by id
    @rpc(Integer, _returns=Module)
    def get_module_by_id(ctx, module_id):
        scoped_session = start_engine()
        session = scoped_session()
        facade = ModuleFacade(session)
        module = facade.get_module_by_id(module_id)
        session.close()
        return module

# return all modules in db
    @rpc(_returns=Iterable(Module))
    def get_all_modules(ctx):
        scoped_session = start_engine()
        session = scoped_session()
        facade = ModuleFacade(session)
        modules = facade.get_all()
        session.close()
        return modules
