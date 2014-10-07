from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from uuid import uuid4


class Param(Base):
    __tablename__ = 'param'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    value = Column(String(120), nullable=False)

    application = Column(Integer, ForeignKey('application.id'))

    def __init__(self, name, value):
        self.name = name
        self.value = value


class Application(Base):
    __tablename__ = 'application'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    serial = Column(String(3244), unique=True)

    param = relationship(Param, backref="params")

    def __init__(self, name):
        self.name = name
        self.serial = uuid4().hex

    def __repr__(self):
        return '<projeto %r>' % self.name

