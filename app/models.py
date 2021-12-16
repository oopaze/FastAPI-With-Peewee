from datetime import datetime

from peewee import Model, CharField, DateTimeField

from . import pwd_context as pwd, db


class BaseModel(Model):
    criado_em = DateTimeField(default=datetime.now)
    atualizado_em = DateTimeField()

    def save(self, *args, **kwargs):
        self.atualizado_em = datetime.now()
        return super().save(*args, **kwargs)

    class Meta:
        database = db


class User(BaseModel):
    nome = CharField(max_length=50)
    username = CharField(max_length=50)
    senha = CharField(max_length=100)
    cpf = CharField(max_length=20)
    rg = CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        kwargs['senha'] = User.gerar_senha_em_hash(kwargs.get('senha', 'mae123'))
        super().__init__(*args, **kwargs)

    def __iter__(self):
        yield "id", self.id
        yield "nome", self.nome
        yield "username", self.username
        yield "cpf", self.cpf
        yield "rg", self.rg
        yield "criado_em", self.criado_em
        yield "atualizado_em", self.atualizado_em

    @staticmethod
    def gerar_senha_em_hash(senha):
        return pwd.hash(senha)

    def verificar_senha(self, senha):
        return pwd.verify(senha, self.senha)

    class Meta:
        table_name = 'usuarios'
