from pydantic import BaseModel # type: ignore
from typing import Optional

class ProdutoEstanteria(BaseModel):
    id_estanteria_producto: Optional[int] =None
    id_estanteria: int
    id_producto: int
    id_pasillo: int
    cantidad: int

class ProductoSearch(BaseModel):
    id_sucursal: int
    codigo_producto: str
    nombre: str