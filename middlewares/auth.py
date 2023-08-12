from fastapi import HTTPException
from fastapi import Header
from jose import jwt, JWTError
from settings import SECRET_KEY
from settings import JWT
from utils import messages


async def validate_authorization(authorization: str = Header()):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail=messages.invalid_auth)
    try:
        payload = jwt.decode(authorization.split('Bearer ')[1], SECRET_KEY,
                             algorithms=[JWT.get('ALGORITHM')])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail=messages.invalid_jwt
        )
