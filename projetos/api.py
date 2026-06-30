from typing import List
from ninja import NinjaAPI
from django.shortcuts import get_object_or_404

from .models import Investigador, Projeto, Entregavel
from .schemas import (
    InvestigadorIn, InvestigadorOut,
    ProjetoIn, ProjetoOut,
    EntregavelIn, EntregavelOut,
)

api = NinjaAPI(title="Projetos API", urls_namespace="projetos_api")


# ---------- INVESTIGADORES ----------

@api.get("/investigadores", response=List[InvestigadorOut], tags=["Investigadores"])
def list_investigadores(request, search: str = "", limit: int = 10, offset: int = 0):
    qs = Investigador.objects.all()
    if search:
        qs = qs.filter(nome__icontains=search)
    return qs[offset:offset + limit]

@api.post("/investigadores", response=InvestigadorOut, tags=["Investigadores"])
def create_investigador(request, payload: InvestigadorIn):
    return Investigador.objects.create(**payload.dict())

@api.get("/investigadores/{investigador_id}", response=InvestigadorOut, tags=["Investigadores"])
def get_investigador(request, investigador_id: int):
    return get_object_or_404(Investigador, id=investigador_id)

@api.put("/investigadores/{investigador_id}", response=InvestigadorOut, tags=["Investigadores"])
def update_investigador(request, investigador_id: int, payload: InvestigadorIn):
    inv = get_object_or_404(Investigador, id=investigador_id)
    for attr, value in payload.dict().items():
        setattr(inv, attr, value)
    inv.save()
    return inv

@api.delete("/investigadores/{investigador_id}", tags=["Investigadores"])
def delete_investigador(request, investigador_id: int):
    get_object_or_404(Investigador, id=investigador_id).delete()
    return {"success": True}


# ---------- PROJETOS ----------

@api.get("/projetos", response=List[ProjetoOut], tags=["Projetos"])
def list_projetos(request, search: str = "", order_by: str = "titulo", limit: int = 10, offset: int = 0):
    qs = Projeto.objects.all()
    if search:
        qs = qs.filter(titulo__icontains=search)
    allowed = ["titulo", "data_inicio", "-titulo", "-data_inicio"]
    if order_by not in allowed:
        order_by = "titulo"
    qs = qs.order_by(order_by)
    return qs[offset:offset + limit]

@api.post("/projetos", response=ProjetoOut, tags=["Projetos"])
def create_projeto(request, payload: ProjetoIn):
    data = payload.dict()
    investigador_ids = data.pop("investigador_ids", [])
    projeto = Projeto.objects.create(**data)
    projeto.investigadores.set(investigador_ids)
    return projeto

@api.get("/projetos/{projeto_id}", response=ProjetoOut, tags=["Projetos"])
def get_projeto(request, projeto_id: int):
    return get_object_or_404(Projeto, id=projeto_id)

@api.put("/projetos/{projeto_id}", response=ProjetoOut, tags=["Projetos"])
def update_projeto(request, projeto_id: int, payload: ProjetoIn):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    data = payload.dict()
    investigador_ids = data.pop("investigador_ids", [])
    for attr, value in data.items():
        setattr(projeto, attr, value)
    projeto.save()
    projeto.investigadores.set(investigador_ids)
    return projeto

@api.delete("/projetos/{projeto_id}", tags=["Projetos"])
def delete_projeto(request, projeto_id: int):
    get_object_or_404(Projeto, id=projeto_id).delete()
    return {"success": True}


# ---------- ENTREGAVEIS ----------

@api.get("/entregaveis", response=List[EntregavelOut], tags=["Entregaveis"])
def list_entregaveis(request, projeto_id: int = None, limit: int = 10, offset: int = 0):
    qs = Entregavel.objects.all()
    if projeto_id:
        qs = qs.filter(projeto_id=projeto_id)
    return qs[offset:offset + limit]

@api.post("/entregaveis", response=EntregavelOut, tags=["Entregaveis"])
def create_entregavel(request, payload: EntregavelIn):
    return Entregavel.objects.create(**payload.dict())

@api.get("/entregaveis/{entregavel_id}", response=EntregavelOut, tags=["Entregaveis"])
def get_entregavel(request, entregavel_id: int):
    return get_object_or_404(Entregavel, id=entregavel_id)

@api.put("/entregaveis/{entregavel_id}", response=EntregavelOut, tags=["Entregaveis"])
def update_entregavel(request, entregavel_id: int, payload: EntregavelIn):
    ent = get_object_or_404(Entregavel, id=entregavel_id)
    for attr, value in payload.dict().items():
        setattr(ent, attr, value)
    ent.save()
    return ent

@api.delete("/entregaveis/{entregavel_id}", tags=["Entregaveis"])
def delete_entregavel(request, entregavel_id: int):
    get_object_or_404(Entregavel, id=entregavel_id).delete()
    return {"success": True}