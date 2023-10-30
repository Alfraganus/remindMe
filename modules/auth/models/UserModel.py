from fastapi import Body
from pydantic import BaseModel, Field
from sqlalchemy import Table, Column, Integer, String, Boolean
from config.db import meta
from sql_app.sql_app import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False)
    name = Column(String(255))
    surname = Column(String(255))
    password = Column(String(500))
    # Add other columns as needed, s

class UserModel():
    users = Table(
        'users', meta,
        Column('id', Integer, primary_key=True),
        Column('username', String(255), nullable=False),
        Column('name', String(255)),
        Column('surname', String(255)),
        Column('password', String(500)),
        # Column('is_active', Boolean()),
    )

class UserResponse(BaseModel):
    username: str
    name: str
    surname: str


class UserCreate(BaseModel):
    username: str
    name: str
    surname: str
    password: str