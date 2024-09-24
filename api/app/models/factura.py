from datetime import date
from tokenize import Double
from pydantic import BaseModel # type: ignore
from typing import List, Optional

class ProductoFactura(BaseModel):
    id_producto: int
    codigo: str
    nombre: str
    cantidad: int
    precio: str  
    subtotal: float  
    subtotalDescuento: float  


class Factura(BaseModel):
    id_sucursal: int
    id_cajero: int
    id_cliente: int
    total: str
    descuento: Optional[str] = None
    listProduct: List[ProductoFactura] 