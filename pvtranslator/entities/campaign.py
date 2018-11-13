from spyne import UnsignedInteger32, Unicode, Date
from pvtranslator.tableModel import TableModel


class Campaign(TableModel):
    __tablename__ = 'campaign'
    __namespace__ = 'pvtranslator'

    id = UnsignedInteger32(pk=True)
    name = Unicode(32, unique=True, nullable=False)
    date = Date(nullable=False)
    module_id = UnsignedInteger32(fk="module.id", nullable=False)

    def __repr__(self):
        return "<Campaign(name='" + str(self.name) + "', date='" + str(self.date) + "')>"
