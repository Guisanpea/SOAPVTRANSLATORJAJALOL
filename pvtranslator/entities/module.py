from spyne import UnsignedInteger32, Unicode,Iterable
from pvtranslator.tableModel import TableModel
from pvtranslator.entities.campaign import Campaign


class Module(TableModel):
    __tablename__ = 'module'
    __namespace__ = 'pvtranslator'

    id = UnsignedInteger32(pk=True)
    name = Unicode(32,unique=True,nullable=False)

    def __repr__(self):
        return "Module(name='%s')" % self.name
