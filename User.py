from sqlalchemy import Boolean, Column, Integer, String
from sql_app.sql_app import Base


class UserModel():
    class User(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True, index=True)
        username = Column(String, unique=True, index=True)
        password = Column(String, unique=True, index=True)
        is_active = Column(Boolean, default=True)
