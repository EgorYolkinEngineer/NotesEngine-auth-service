from fastapi import APIRouter, Depends

from middlewares.auth import validate_authorization
from utils.tools import make_jwt
from utils import messages
from fastapi import HTTPException
from models import LoginData, RegisterData, UserModel, JWTModel
from core.db_models import *
from core.database import session
from base.passwords import check_password, hash_password

user_router = APIRouter()


@user_router.post('/auth/register/',
                  response_model=JWTModel,
                  description='Register user')
async def register_user(register_data: RegisterData):
    hashed_password = hash_password(register_data.password)

    user = User(
        username=register_data.username,
        name=register_data.name,
        surname=register_data.surname,
        age=register_data.age,
        hashed_password=hashed_password
    )
    session.add(user)
    session.commit()

    jwt_data = {
        'user_id': user.id,
        'username': user.username
    }

    return make_jwt(jwt_data)


@user_router.post('/auth/login/',
                  response_model=JWTModel,
                  description='Login user')
async def login_user(login_data: LoginData):
    data = session.query(User).filter_by(username=login_data.username).first()

    if not data:
        return HTTPException(
            status_code=401,
            detail=messages.incorrect_auth_data
        )
    elif not check_password(login_data.password, data.hashed_password):
        return HTTPException(
            status_code=401,
            detail=messages.incorrect_auth_data
        )

    jwt_data = {
        'user_id': data.id,
        'username': data.username
    }

    return make_jwt(jwt_data)


@user_router.get('/user/me/',
                 response_model=UserModel,
                 description='Get current user info')
async def user_me(access_token: str | dict = Depends(validate_authorization)):
    user = session.query(User).filter_by(id=access_token.get('user_id')).first()

    return user.to_dict(exclude=['hashed_password'])
