from ninja import Schema
from datetime import date
from typing import List


class InvestigadorIn(Schema):
    nome: str

class InvestigadorOut(Schema):
    id: int
    nome: str


class EntregavelIn(Schema):
    tipo: str
    data_entrega: date
    link: str
    projeto_id: int

class EntregavelOut(Schema):
    id: int
    tipo: str
    data_entrega: date
    link: str
    projeto_id: int


class ProjetoIn(Schema):
    titulo: str
    resumo: str
    data_inicio: date
    coordenador_id: int
    investigador_ids: List[int] = []

class ProjetoOut(Schema):
    id: int
    titulo: str
    resumo: str
    data_inicio: date
    coordenador_id: int