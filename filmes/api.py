from typing import List
from ninja import NinjaAPI
from django.shortcuts import get_object_or_404

from .models import Ator, Filme, Utilizador, Classificacao
from .schemas import (
    AtorIn, AtorOut,
    FilmeIn, FilmeOut,
    UtilizadorIn, UtilizadorOut,
    ClassificacaoIn, ClassificacaoOut,
)

api = NinjaAPI(title="Filmes API", urls_namespace="filmes_api")


# ---------- ATORES ----------

@api.get("/atores", response=List[AtorOut], tags=["Atores"])
def list_atores(request, search: str = "", limit: int = 10, offset: int = 0):
    qs = Ator.objects.all()
    if search:
        qs = qs.filter(nome__icontains=search)
    return qs[offset:offset + limit]

@api.post("/atores", response=AtorOut, tags=["Atores"])
def create_ator(request, payload: AtorIn):
    return Ator.objects.create(**payload.dict())

@api.get("/atores/{ator_id}", response=AtorOut, tags=["Atores"])
def get_ator(request, ator_id: int):
    return get_object_or_404(Ator, id=ator_id)

@api.delete("/atores/{ator_id}", tags=["Atores"])
def delete_ator(request, ator_id: int):
    get_object_or_404(Ator, id=ator_id).delete()
    return {"success": True}


# ---------- FILMES ----------

@api.get("/filmes", response=List[FilmeOut], tags=["Filmes"])
def list_filmes(request, search: str = "", pais: str = "", limit: int = 10, offset: int = 0):
    qs = Filme.objects.all()
    if search:
        qs = qs.filter(titulo__icontains=search)
    if pais:
        qs = qs.filter(pais__icontains=pais)
    return qs[offset:offset + limit]

@api.post("/filmes", response=FilmeOut, tags=["Filmes"])
def create_filme(request, payload: FilmeIn):
    data = payload.dict()
    ator_ids = data.pop("ator_ids", [])
    filme = Filme.objects.create(**data)
    filme.atores.set(ator_ids)
    return filme

@api.get("/filmes/{filme_id}", response=FilmeOut, tags=["Filmes"])
def get_filme(request, filme_id: int):
    return get_object_or_404(Filme, id=filme_id)

@api.put("/filmes/{filme_id}", response=FilmeOut, tags=["Filmes"])
def update_filme(request, filme_id: int, payload: FilmeIn):
    filme = get_object_or_404(Filme, id=filme_id)
    data = payload.dict()
    ator_ids = data.pop("ator_ids", [])
    for attr, value in data.items():
        setattr(filme, attr, value)
    filme.save()
    filme.atores.set(ator_ids)
    return filme

@api.delete("/filmes/{filme_id}", tags=["Filmes"])
def delete_filme(request, filme_id: int):
    get_object_or_404(Filme, id=filme_id).delete()
    return {"success": True}


# ---------- UTILIZADORES ----------

@api.get("/utilizadores", response=List[UtilizadorOut], tags=["Utilizadores"])
def list_utilizadores(request, limit: int = 10, offset: int = 0):
    return Utilizador.objects.all()[offset:offset + limit]

@api.post("/utilizadores", response=UtilizadorOut, tags=["Utilizadores"])
def create_utilizador(request, payload: UtilizadorIn):
    return Utilizador.objects.create(**payload.dict())

@api.get("/utilizadores/{utilizador_id}", response=UtilizadorOut, tags=["Utilizadores"])
def get_utilizador(request, utilizador_id: int):
    return get_object_or_404(Utilizador, id=utilizador_id)

@api.delete("/utilizadores/{utilizador_id}", tags=["Utilizadores"])
def delete_utilizador(request, utilizador_id: int):
    get_object_or_404(Utilizador, id=utilizador_id).delete()
    return {"success": True}


# ---------- CLASSIFICACOES ----------

@api.get("/classificacoes", response=List[ClassificacaoOut], tags=["Classificacoes"])
def list_classificacoes(request, filme_id: int = None, utilizador_id: int = None, limit: int = 10, offset: int = 0):
    qs = Classificacao.objects.all()
    if filme_id:
        qs = qs.filter(filme_id=filme_id)
    if utilizador_id:
        qs = qs.filter(utilizador_id=utilizador_id)
    return qs[offset:offset + limit]

@api.post("/classificacoes", response=ClassificacaoOut, tags=["Classificacoes"])
def create_classificacao(request, payload: ClassificacaoIn):
    return Classificacao.objects.create(**payload.dict())

@api.get("/classificacoes/{classificacao_id}", response=ClassificacaoOut, tags=["Classificacoes"])
def get_classificacao(request, classificacao_id: int):
    return get_object_or_404(Classificacao, id=classificacao_id)

@api.delete("/classificacoes/{classificacao_id}", tags=["Classificacoes"])
def delete_classificacao(request, classificacao_id: int):
    get_object_or_404(Classificacao, id=classificacao_id).delete()
    return {"success": True}