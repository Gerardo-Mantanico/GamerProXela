from fastapi import APIRouter, HTTPException
from ..db.db import session
from ..models.sucursales import Sucursal
from ..services import sucursal_s

def router_api(nombre: str) -> APIRouter:
    router = APIRouter(
        prefix="/"+nombre,
        tags=[nombre],
        responses={404: {"description": "Not found"}},
    )
    return router
