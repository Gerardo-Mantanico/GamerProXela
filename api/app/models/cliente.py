from pydantic import BaseModel # type: ignore
from typing import Optional

class Cliente(BaseModel):
    id_cliente: Optional[int] = None
    nombre: str
    nit: str
    telefono: int
    direccion: str
