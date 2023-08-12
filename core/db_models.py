from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from core.db_mixins import SerializerMixin

Base = declarative_base()


class User(Base, SerializerMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    hashed_password = Column(String)

