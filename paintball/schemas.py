from ninja import Schema
from datetime import date
from decimal import Decimal
from typing import List


class EventIn(Schema):
    name: str
    date: date
    location: str
    price: Decimal
    description: str = ""


class EventOut(Schema):
    id: int
    name: str
    date: date
    location: str
    price: Decimal
    description: str


class ParticipantIn(Schema):
    name: str
    email: str
    age: int
    event_id: int


class ParticipantOut(Schema):
    id: int
    name: str
    email: str
    age: int
    event_id: int


class TeamIn(Schema):
    name: str
    color: str
    participant_ids: List[int] = []


class TeamOut(Schema):
    id: int
    name: str
    color: str