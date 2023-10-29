from sqlalchemy import Table, Column, Integer, String, Boolean
from config.db import meta

users = Table(
    'users',meta,
    Column('id', Integer, primary_key=True),
    Column('username', String(255), nullable=False),
    Column('name', String(255)),
    Column('surname', String(255)),
    Column('password', String(500)),
    # Column('is_active', Boolean()),
)