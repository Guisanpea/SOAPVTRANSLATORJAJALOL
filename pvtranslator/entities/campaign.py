from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from pvtranslator.base import Base


class Campaign(Base):
    __tablename__ = 'campaign'

    id = Column(Integer, primary_key=True)
    name = Column(String(30),nullable=False)
    date = Column(Date,nullable=False)
    module_id = Column(Integer, ForeignKey("module.id"),nullable=False)
    module = relationship("Module", back_populates="campaigns", cascade="save-update")

    def __repr__(self):
        return "<Campaign(name='" + str(self.name) + "', date='" + str(self.date) + "')>"
