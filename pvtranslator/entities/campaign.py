from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from pvtranslator.base import Base


class Campaign(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(Date)
    module_id = Column(Integer, ForeignKey('module.id'))

    module = relationship("Module", back_populates="modules")

    def __repr__(self):
        return "<Campaign(name='" + str(self.name) + "', date='" + str(self.date) + "')>"
