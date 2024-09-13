from pydantic import BaseModel # type: ignore
from typing import Optional

class ProductoBodega(BaseModel):
    id_producto_bodega: Optional[int] =None
    id_bodega: int
    id_producto: int
    cantidad: int