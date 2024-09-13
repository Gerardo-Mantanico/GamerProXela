from pydantic import BaseModel # type: ignore
from typing import Optional

class Bodega(BaseModel):
    id_bodega : Optional[int] =None
    id_empleado: int
    id_sucursal: int