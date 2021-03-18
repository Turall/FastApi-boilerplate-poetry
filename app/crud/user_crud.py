from typing import List, Union
from uuid import UUID
from fastapi import HTTPException, status
from app.data.models import Users
from app.controllers.schemas import UserSchema, UserSchemaDB, UserUpdateSchema
from app.utils.helpers import clean_dict


async def create_user(data: UserSchema) :
    """ 
        create Users, check email address.  if exist raise Exception

    """
    if await Users.exists(Users.email == data.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    user = await Users.create(**data.dict())


async def get_users() -> List[UserSchemaDB]:
    """ Get all Users data """

    return await Users.query.gino.all()


async def get_user_by_id(user_id: UUID):
    """ 
        Get User data with given id. If not found raise Exception 
    
    """
    return await Users.get_or_404(user_id)


async def update_user(user_id: UUID, data: UserUpdateSchema) -> UserSchemaDB:
    user = await get_user_by_id(user_id)
    await user.update(**clean_dict(data.dict())).apply()
    return user


async def delete_user(user_id: UUID) -> None:
    """ Delete user from db with given id. If user doesn't exist raise exception """
    try:
        user = await Users.get_or_404(user_id)
        await user.delete()
    except Exception as _:
        pass
