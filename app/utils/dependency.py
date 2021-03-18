from jose import jwt
from jose.exceptions import JOSEError
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasicCredentials
from core.factories import settings
from core.extensions import security





async def has_access(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Function for validation JWT token in header
    """
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            key=settings.SECRET_KEY,
            options={
                "verify_signature": False,
                "verify_aud": False,
                "verify_iss": False,
            },
        )
        print("payload --> ", payload)
    except JOSEError as e:
        raise HTTPException(status_code=409, detail=str(e))
