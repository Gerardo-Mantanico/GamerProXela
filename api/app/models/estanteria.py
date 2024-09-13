from pydantic import BaseModel # type: ignore
from typing import Optional

class Estanteria(BaseModel):
    id_estanteria: Optional[int] = None
    id_sucursal: int
    id_empleado: int
    