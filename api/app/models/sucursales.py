from pydantic import BaseModel # type: ignore
from typing import Optional
from datetime import time


class Sucursal(BaseModel):
    id: Optional[int] = None
    direccion: str
    nombre: str
    no_sucursal:int
    codigo: str
    correo: str
    telefono: int
    horario_apertura: time 
    horario_cierre: time


