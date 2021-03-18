from typing import Union
from fastapi import HTTPException, status
# from app.data.models import Users
from app.controllers.schemas import UserSchema
# from core.extensions import db



def clean_dict(data: dict) -> dict:
    return {key: val for (key, val) in data.items() if val is not None}


async def get_user_by_email(email: str) -> Union[HTTPException,UserSchema]:
    """ 
        check user with this email address exist in db or not. 
        If exist return user object else raise exception.
    
    """

    # if (user := await Users.query.where(Users.email == email).gino.first()) is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    # return user
    pass


async def check_db_status() -> bool:
    """ for check database we will execute raw query. """
    try:
        await db.status('SELECT 1')
        return True
    except:
        return False