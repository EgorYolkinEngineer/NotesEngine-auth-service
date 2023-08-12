from fastapi import HTTPException, Depends, APIRouter
from middlewares.auth import validate_authorization
from utils.tools import make_jwt
from utils import messages
from models import JWTModel

jwt_router = APIRouter()


@jwt_router.get('/auth/jwt/refresh/',
                description='Refresh access JWT' ,
                response_model=JWTModel)
async def refresh_jwt(refresh_token: str | dict = Depends(validate_authorization)):
    if refresh_token.get('is_access'):
        return HTTPException(
            status_code=401,
            detail=messages.jwt_is_access
        )
    jwt_data = {
        'user_id': refresh_token.get('user_id'),
        'username': refresh_token.get('username')
    }

    return make_jwt(jwt_data)
