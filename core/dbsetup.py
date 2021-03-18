from uuid import uuid4
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from core.extensions import db


Column,Integer,String,BOOLEAN,ForeignKey,Datetime = db.Column,db.Integer,db.String,db.BOOLEAN,db.ForeignKey,db.DateTime


class SurrogatePK(object):
    """A mixin that adds a surrogate UUID 'primary key' column named ``id`` to
    any declarative-mapped class."""

    __table_args__ = {"extend_existing": True}

    id = Column(UUIDType(binary=False), primary_key=True,default=str(uuid4()))
    created = Column(Datetime(), default=func.now())
    updated = Column(Datetime(), onupdate=func.now())


class Model(SurrogatePK,db.Model):
    __abstract__ = True

    @classmethod
    async def exists(cls, *args):
        obj = await cls.query.where(*args).gino.first()
        if not obj:
            return False
        return True