from pydantic import BaseModel # type: ignore
from typing import Optional

class ProdutoEstanteria(BaseModel):
    id_estanteria_producto: Optional[int] =None
    id_estanteria: int
    id_producto_bodega: int
    no_pasillo: str