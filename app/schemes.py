from datetime import datetime
from pydantic import BaseModel


class UserReadingModel(BaseModel):
    id: str
    nome: str
    username: str

    criado_em: datetime
    atualizado_em: datetime

    class Meta:
        orm_meta = True
