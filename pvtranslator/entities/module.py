from spyne import UnsignedInteger32, Unicode, Array, table
from pvtranslator.tableModel import TableModel
from pvtranslator.entities.campaign import Campaign


class Module(TableModel):
    __tablename__ = 'module'
    __namespace__ = 'pvtranslator'

    id = UnsignedInteger32(pk=True)
    name = Unicode(32,unique=True,nullable=False)
    campaigns = Array(Campaign).store_as(table(right='module_id'))

    def __repr__(self):
        return "Module(name='%s')" % self.name
