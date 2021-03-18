from typing import List, Union
from uuid import UUID
from fastapi import APIRouter, Path, Body, Query
from starlette.responses import JSONResponse
from app.controllers.schemas import (
    TestErrorSchema,
    TestSchema,
    UserSchema,
    UserSchemaDB, UserUpdateSchema,
)
from app.crud.user_crud import create_user, delete_user, get_users, get_user_by_id, update_user


router = APIRouter(prefix="/protected/users")


@router.post(
    "/simple-body-data",
    response_description="custom response description",
    description="custom description for this endpoint",
    response_model=UserSchemaDB,
    responses={404: {"model": TestErrorSchema}},
)
async def test_body(
    payload: dict = Body(
        ...,
        example={
            "name": "string",
            "surname": "string",
            "email": "string@string.string",
        },
    )
) -> JSONResponse:
    print(payload)
    if payload:
        return await create_user(payload)
    return JSONResponse({"result": True})


@router.post(
    "/schema-body-data",
    response_description="custom response description",
    description="custom description for this endpoint",
    response_model=UserSchemaDB,
    responses={404: {"model": TestErrorSchema}},
)
async def test_body_withschema(payload: UserSchema):
    return await create_user(payload)



@router.get(
    "/",
    response_description="custom response description",
    description="custom description for this endpoint",
    response_model=List[UserSchemaDB],
    responses={404: {"model": TestErrorSchema}},
)
async def fetch_users(filter: str= Query(None, alias="aliasfilter", title="filterTitle", description="Send filter in the query")):
    return await get_users()


@router.get(
    "/{id}",
    response_description="custom response description",
    description="custom description for this endpoint",
    response_model=UserSchemaDB,
    responses={404: {"model": TestErrorSchema}},
)
async def fetch_user(id: UUID):
    return await get_user_by_id(id)


@router.put(
    "/{id}",
    response_description="custom response description",
    description="custom description for this endpoint",
    response_model=UserSchemaDB,
    responses={404: {"model": TestErrorSchema}},
)
async def update_users_info(data: UserUpdateSchema, id: UUID = Path(...,description="User id for update")):
    return await update_user(id,data)


@router.delete(
    "/{id}",
    response_description="custom response description",
    description="custom description for this endpoint",
    responses={404: {"model": TestErrorSchema}},
)
async def fetch_user(id: UUID):
    return await delete_user(id)
