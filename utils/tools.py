from datetime import datetime, timedelta
from jose import jwt
from settings import (JWT, SECRET_KEY)
import random


def generate_nickname():
    words = ["Lion", "Star", "Fire", "Ice", "Shadow", "Storm", "Dream", "Silver", "Ruby", "Crimson",
             "Phoenix", "Dragon", "Whisper", "Midnight", "Mystic", "Aurora", "Willow", "Velvet",
             "Sapphire", "Ember"]
    word = random.choice(words)
    numbers = random.randint(10, 999)  # Генерируем двух-трехзначное число
    nickname = f"{word}{numbers}"
    return nickname


def create_jwt(data: dict, is_access: bool = True):
    to_encode = data.copy()

    if is_access:
        expire = datetime.utcnow() + timedelta(minutes=JWT.get('JWT_ACCESS_EXPIRE_TIME'))
    else:
        expire = datetime.utcnow() + timedelta(minutes=JWT.get('JWT_REFRESH_EXPIRE_TIME'))

    to_encode.update(
        {
            'exp': expire,
            'is_access': True if is_access else False,
        }
    )
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=JWT.get('ALGORITHM'))

    return encoded_jwt


def make_jwt(jwt_data: dict) -> dict:
    return {
        'access_token': create_jwt(jwt_data),
        'refresh_token': create_jwt(jwt_data, is_access=False)
    }
