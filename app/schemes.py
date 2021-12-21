from typing import Any
from datetime import datetime

from pydantic import BaseModel


class UserReadingModel(BaseModel):
    id: str
    nome: str
    username: str

    criado_em: datetime
    atualizado_em: datetime

    class Config:
        orm_mode = True
