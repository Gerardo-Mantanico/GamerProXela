from datetime import date
from tokenize import Double
from pydantic import BaseModel # type: ignore
from typing import Optional

class Factura(BaseModel):
    id_sucursal: int
    id_empleado: int
    id_cliente: int
    total: float
    nit: str
    nombre: str
    direccion: str
    telefono: str
    descuento_aplicado: float
    Detalles_facutura = []

class Detalles_facutura(BaseModel):
    codigo: str
    nombre: str
    cantidad: int;
    precio: str;
    subtotal: int
    subtotalDescuento: int

    