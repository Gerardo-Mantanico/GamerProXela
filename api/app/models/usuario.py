from pydantic import BaseModel # type: ignore
from typing import Optional

class Usuario(BaseModel):
    id: Optional[int] = None
    rol: str
    usuario: str
    password: str
    id_sucursal: int
    nombre: str
    telefono: int
    correo: str

class Cajero (Usuario):
    no_caja:int

