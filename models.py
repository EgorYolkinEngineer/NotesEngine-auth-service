from pydantic import BaseModel
from utils.tools import generate_nickname


class JWTData(BaseModel):
    info: str
    username: str = generate_nickname()


class JWTModel(BaseModel):
    access_token: str
    refresh_token: str


class LoginData(BaseModel):
    username: str
    password: str


class RegisterData(BaseModel):
    username: str
    password: str
    name: str
    surname: str
    age: int


class UserModel(BaseModel):
    username: str
    name: str
    surname: str
    age: int
