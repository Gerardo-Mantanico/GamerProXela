from sqlalchemy.orm  import Session
from ..models.sucursales import Sucursal

def create_sucursales(session:Session, nombre: str, direccion: str):
    sucursal = Sucursal(nombre=nombre, direccion=direccion)
    session.add(sucursal)
    session.commit()
    return sucursal

