from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from pvtranslator.base import Base


class Module(Base):
    __tablename__ = 'module'

    id = Column(Integer, primary_key=True)
    name = Column(String(30),nullable=False)
    campaigns = relationship("Campaign", back_populates="module", cascade="all, delete-orphan")

    def __repr__(self):
        return "Module(name='%s')" % self.name
