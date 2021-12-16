from fastapi import FastAPI
from passlib.context import CryptContext
from peewee import SqliteDatabase


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
db = SqliteDatabase('storage.db')


def create_app():
    app = FastAPI()

    db.connect()

    from .routes import user_router

    app.include_router(user_router, responses={404: {'description': 'not found'}})

    from .models import User

    User.create_table()

    return app
