from typing import List
from ninja import NinjaAPI
from django.shortcuts import get_object_or_404

from .models import Cliente, Prato, Restaurante, Reserva
from .schemas import (
    ClienteIn, ClienteOut,
    PratoIn, PratoOut,
    RestauranteIn, RestauranteOut,
    ReservaIn, ReservaOut,
)

api = NinjaAPI(title="Restaurante API", urls_namespace="restaurante_api")


# ---------- CLIENTES ----------

@api.get("/clientes", response=List[ClienteOut], tags=["Clientes"])
def list_clientes(request, search: str = "", limit: int = 10, offset: int = 0):
    qs = Cliente.objects.all()
    if search:
        qs = qs.filter(nome__icontains=search)
    return qs[offset:offset + limit]

@api.post("/clientes", response=ClienteOut, tags=["Clientes"])
def create_cliente(request, payload: ClienteIn):
    return Cliente.objects.create(**payload.dict())

@api.get("/clientes/{cliente_id}", response=ClienteOut, tags=["Clientes"])
def get_cliente(request, cliente_id: int):
    return get_object_or_404(Cliente, id=cliente_id)

@api.put("/clientes/{cliente_id}", response=ClienteOut, tags=["Clientes"])
def update_cliente(request, cliente_id: int, payload: ClienteIn):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    for attr, value in payload.dict().items():
        setattr(cliente, attr, value)
    cliente.save()
    return cliente

@api.delete("/clientes/{cliente_id}", tags=["Clientes"])
def delete_cliente(request, cliente_id: int):
    get_object_or_404(Cliente, id=cliente_id).delete()
    return {"success": True}


# ---------- PRATOS ----------

@api.get("/pratos", response=List[PratoOut], tags=["Pratos"])
def list_pratos(request, search: str = "", limit: int = 10, offset: int = 0):
    qs = Prato.objects.all()
    if search:
        qs = qs.filter(nome__icontains=search)
    return qs[offset:offset + limit]

@api.post("/pratos", response=PratoOut, tags=["Pratos"])
def create_prato(request, payload: PratoIn):
    return Prato.objects.create(**payload.dict())

@api.get("/pratos/{prato_id}", response=PratoOut, tags=["Pratos"])
def get_prato(request, prato_id: int):
    return get_object_or_404(Prato, id=prato_id)

@api.delete("/pratos/{prato_id}", tags=["Pratos"])
def delete_prato(request, prato_id: int):
    get_object_or_404(Prato, id=prato_id).delete()
    return {"success": True}


# ---------- RESTAURANTES ----------

@api.get("/restaurantes", response=List[RestauranteOut], tags=["Restaurantes"])
def list_restaurantes(request, search: str = "", limit: int = 10, offset: int = 0):
    qs = Restaurante.objects.all()
    if search:
        qs = qs.filter(nome__icontains=search)
    return qs[offset:offset + limit]

@api.post("/restaurantes", response=RestauranteOut, tags=["Restaurantes"])
def create_restaurante(request, payload: RestauranteIn):
    data = payload.dict()
    prato_ids = data.pop("prato_ids", [])
    restaurante = Restaurante.objects.create(**data)
    restaurante.menu.set(prato_ids)
    return restaurante

@api.get("/restaurantes/{restaurante_id}", response=RestauranteOut, tags=["Restaurantes"])
def get_restaurante(request, restaurante_id: int):
    return get_object_or_404(Restaurante, id=restaurante_id)

@api.put("/restaurantes/{restaurante_id}", response=RestauranteOut, tags=["Restaurantes"])
def update_restaurante(request, restaurante_id: int, payload: RestauranteIn):
    restaurante = get_object_or_404(Restaurante, id=restaurante_id)
    data = payload.dict()
    prato_ids = data.pop("prato_ids", [])
    for attr, value in data.items():
        setattr(restaurante, attr, value)
    restaurante.save()
    restaurante.menu.set(prato_ids)
    return restaurante

@api.delete("/restaurantes/{restaurante_id}", tags=["Restaurantes"])
def delete_restaurante(request, restaurante_id: int):
    get_object_or_404(Restaurante, id=restaurante_id).delete()
    return {"success": True}


# ---------- RESERVAS ----------

@api.get("/reservas", response=List[ReservaOut], tags=["Reservas"])
def list_reservas(request, cliente_id: int = None, restaurante_id: int = None, limit: int = 10, offset: int = 0):
    qs = Reserva.objects.all()
    if cliente_id:
        qs = qs.filter(cliente_id=cliente_id)
    if restaurante_id:
        qs = qs.filter(restaurante_id=restaurante_id)
    return qs[offset:offset + limit]

@api.post("/reservas", response=ReservaOut, tags=["Reservas"])
def create_reserva(request, payload: ReservaIn):
    return Reserva.objects.create(**payload.dict())

@api.get("/reservas/{reserva_id}", response=ReservaOut, tags=["Reservas"])
def get_reserva(request, reserva_id: int):
    return get_object_or_404(Reserva, id=reserva_id)

@api.put("/reservas/{reserva_id}", response=ReservaOut, tags=["Reservas"])
def update_reserva(request, reserva_id: int, payload: ReservaIn):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    for attr, value in payload.dict().items():
        setattr(reserva, attr, value)
    reserva.save()
    return reserva

@api.delete("/reservas/{reserva_id}", tags=["Reservas"])
def delete_reserva(request, reserva_id: int):
    get_object_or_404(Reserva, id=reserva_id).delete()
    return {"success": True}