from pvtranslator.entities.module import Module
from pvtranslator.facades.module_facade import ModuleFacade
from pvtranslator.start import start_engine


def test_create():
    scoped_session = start_engine()
    session = scoped_session()

    # create module
    module = Module(name="sample")
    facade = ModuleFacade(session)
    facade.create_module(module=module)

    # get created module
    query = session.query(Module).filter_by(id=module.id)
    module_query = query.all()

    assert len(module_query) == 1
    assert module_query[0] is module

    session.close()


def test_update():

    scoped_session = start_engine()
    session = scoped_session()

    # get first module
    query = session.query(Module).filter_by(id=1)
    module_query = query.all()
    module = module_query[0]
    module.name = module.name + "_update"

    # update
    facade = ModuleFacade(session)
    facade.update_module(module)

    # get module again
    query = session.query(Module).filter_by(id=1)
    module_query = query.all()

    assert len(module_query) == 1
    assert module_query[0] is module

    session.close()


def test_delete():

    scoped_session = start_engine()
    session = scoped_session()

    # get first module
    query = session.query(Module).filter_by(id=1)
    module_query = query.all()
    module = module_query[0]

    # delete
    facade = ModuleFacade(session)
    facade.delete_module(module)

    # get module again
    query = session.query(Module).filter_by(id=1)
    module_query = query.all()

    assert len(module_query) == 0

    session.close()


def test():
    test_create()
    test_update()
    test_delete()



