from string import ascii_letters, digits
from random import choices
from typing import List
from fastapi import APIRouter

from .schemes import UserReadingModel
from .models import User


user_router = APIRouter()


@user_router.get('/', response_model=List[UserReadingModel])
def get_users() -> List[UserReadingModel]:
    users = User.select()
    return list(users)


@user_router.get('/create/random', response_model=UserReadingModel)
def create_random_user():
    data = {
        "nome": "".join(choices(ascii_letters, k=10)),
        "username": "".join(choices(ascii_letters, k=10)),
        "senha": "".join(choices(ascii_letters + digits, k=10)),
        "cpf": "".join(choices(digits, k=11)),
        "rg": "".join(choices(digits, k=11)),
    }

    instance = User(**data)
    instance.save()

    return instance
