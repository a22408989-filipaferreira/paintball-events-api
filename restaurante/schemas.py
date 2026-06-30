from ninja import Schema
from datetime import date, time
from typing import List


class ClienteIn(Schema):
    nome: str

class ClienteOut(Schema):
    id: int
    nome: str


class PratoIn(Schema):
    nome: str

class PratoOut(Schema):
    id: int
    nome: str


class RestauranteIn(Schema):
    nome: str
    localizacao: str
    capacidade: int
    prato_ids: List[int] = []

class RestauranteOut(Schema):
    id: int
    nome: str
    localizacao: str
    capacidade: int


class ReservaIn(Schema):
    data: date
    hora: time
    numero_pessoas: int
    cliente_id: int
    restaurante_id: int

class ReservaOut(Schema):
    id: int
    data: date
    hora: time
    numero_pessoas: int
    cliente_id: int
    restaurante_id: int