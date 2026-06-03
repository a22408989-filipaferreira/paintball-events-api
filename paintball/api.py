from typing import List
from ninja import NinjaAPI, Query
from django.shortcuts import get_object_or_404

from .models import Event, Participant, Team
from .schemas import (
    EventIn, EventOut,
    ParticipantIn, ParticipantOut,
    TeamIn, TeamOut,
)

api = NinjaAPI(title="Paintball Events API")


# ---------- EVENTS ----------

@api.get("/events", response=List[EventOut])
def list_events(
    request,
    search: str = "",
    location: str = "",
    order_by: str = "name",
    limit: int = 10,
    offset: int = 0
):
    events = Event.objects.all()

    if search:
        events = events.filter(name__icontains=search)

    if location:
        events = events.filter(location__icontains=location)

    allowed_order_fields = ["name", "date", "location", "price", "-name", "-date", "-location", "-price"]

    if order_by not in allowed_order_fields:
        order_by = "name"

    events = events.order_by(order_by)

    return events[offset:offset + limit]


@api.post("/events", response=EventOut)
def create_event(request, payload: EventIn):
    event = Event.objects.create(**payload.dict())
    return event


@api.get("/events/{event_id}", response=EventOut)
def get_event(request, event_id: int):
    return get_object_or_404(Event, id=event_id)


@api.put("/events/{event_id}", response=EventOut)
def update_event(request, event_id: int, payload: EventIn):
    event = get_object_or_404(Event, id=event_id)

    for attr, value in payload.dict().items():
        setattr(event, attr, value)

    event.save()
    return event


@api.delete("/events/{event_id}")
def delete_event(request, event_id: int):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return {"success": True}


# ---------- PARTICIPANTS ----------

@api.get("/participants", response=List[ParticipantOut])
def list_participants(
    request,
    search: str = "",
    event_id: int = None,
    order_by: str = "name",
    limit: int = 10,
    offset: int = 0
):
    participants = Participant.objects.all()

    if search:
        participants = participants.filter(name__icontains=search)

    if event_id:
        participants = participants.filter(event_id=event_id)

    allowed_order_fields = ["name", "age", "email", "-name", "-age", "-email"]

    if order_by not in allowed_order_fields:
        order_by = "name"

    participants = participants.order_by(order_by)

    return participants[offset:offset + limit]


@api.post("/participants", response=ParticipantOut)
def create_participant(request, payload: ParticipantIn):
    participant = Participant.objects.create(**payload.dict())
    return participant


@api.get("/participants/{participant_id}", response=ParticipantOut)
def get_participant(request, participant_id: int):
    return get_object_or_404(Participant, id=participant_id)


@api.put("/participants/{participant_id}", response=ParticipantOut)
def update_participant(request, participant_id: int, payload: ParticipantIn):
    participant = get_object_or_404(Participant, id=participant_id)

    for attr, value in payload.dict().items():
        setattr(participant, attr, value)

    participant.save()
    return participant


@api.delete("/participants/{participant_id}")
def delete_participant(request, participant_id: int):
    participant = get_object_or_404(Participant, id=participant_id)
    participant.delete()
    return {"success": True}


# ---------- TEAMS ----------

@api.get("/teams", response=List[TeamOut])
def list_teams(
    request,
    search: str = "",
    color: str = "",
    order_by: str = "name",
    limit: int = 10,
    offset: int = 0
):
    teams = Team.objects.all()

    if search:
        teams = teams.filter(name__icontains=search)

    if color:
        teams = teams.filter(color__icontains=color)

    allowed_order_fields = ["name", "color", "-name", "-color"]

    if order_by not in allowed_order_fields:
        order_by = "name"

    teams = teams.order_by(order_by)

    return teams[offset:offset + limit]


@api.post("/teams", response=TeamOut)
def create_team(request, payload: TeamIn):
    data = payload.dict()
    participant_ids = data.pop("participant_ids", [])

    team = Team.objects.create(**data)
    team.participants.set(participant_ids)

    return team


@api.get("/teams/{team_id}", response=TeamOut)
def get_team(request, team_id: int):
    return get_object_or_404(Team, id=team_id)


@api.put("/teams/{team_id}", response=TeamOut)
def update_team(request, team_id: int, payload: TeamIn):
    team = get_object_or_404(Team, id=team_id)

    data = payload.dict()
    participant_ids = data.pop("participant_ids", [])

    for attr, value in data.items():
        setattr(team, attr, value)

    team.save()
    team.participants.set(participant_ids)

    return team


@api.delete("/teams/{team_id}")
def delete_team(request, team_id: int):
    team = get_object_or_404(Team, id=team_id)
    team.delete()
    return {"success": True}