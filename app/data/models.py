from core.dbsetup import (
    Column,
    Model,
    String,
)


class Users(Model):
    """ Users model for demo """

    __tablename__ = "users"

    name = Column(String(), nullable=False)
    surname = Column(String(), nullable=False)
    email = Column(String(), nullable=False, index=True)
