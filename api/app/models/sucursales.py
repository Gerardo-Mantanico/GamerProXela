from pydantic import BaseModel # type: ignore
from typing import Optional

class Sucursal(BaseModel):
    id: Optional[int] = None
    direccion: str
    nombre: str
    no_sucursal:int

