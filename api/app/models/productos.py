from pydantic import BaseModel # type: ignore
from typing import Optional
from datetime import date 


class Producto(BaseModel):
    id: Optional[int] = None
    codigo: str
    nombre: str
    descripcion:str
    precio: str
    categoria: int


class Consola(Producto):
    marca: str
    modelo: str


class Videojuegos(Producto):
    genero: str
    fecha_lanzamiento : date
    plataforma : str
    mecanica : str

