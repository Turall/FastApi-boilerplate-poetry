from datetime import datetime
from pydantic import BaseModel, constr, validator, ValidationError, EmailStr
from uuid import UUID
from typing import Optional, List, Union
import pydantic.json
import asyncpg.pgproto.pgproto

pydantic.json.ENCODERS_BY_TYPE[asyncpg.pgproto.pgproto.UUID] = str


class TestSchema(BaseModel):
    test: str
    status_code: int

    class Config:
        schema_extra = {"example": {"test": "Test", "status_code": 200}}


class TestErrorSchema(BaseModel):
    test: str
    status_code: int

    class Config:
        schema_extra = {"example": {"test": "Test Error", "status_code": 404}}


class UserSchema(BaseModel):
    name: str
    surname: str
    email: EmailStr


class UserSchemaDB(UserSchema):
    id: UUID
    created: datetime
    updated: Union[datetime, None] = None

    class Config:
        orm_mode = True


class UserUpdateSchema(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    email: Optional[EmailStr]