from ninja import Schema
from datetime import date
from typing import List


class AtorIn(Schema):
    nome: str

class AtorOut(Schema):
    id: int
    nome: str


class FilmeIn(Schema):
    titulo: str
    data_lancamento: date
    pais: str
    ator_ids: List[int] = []

class FilmeOut(Schema):
    id: int
    titulo: str
    data_lancamento: date
    pais: str


class UtilizadorIn(Schema):
    nome: str

class UtilizadorOut(Schema):
    id: int
    nome: str


class ClassificacaoIn(Schema):
    nota: int
    filme_id: int
    utilizador_id: int

class ClassificacaoOut(Schema):
    id: int
    nota: int
    filme_id: int
    utilizador_id: int