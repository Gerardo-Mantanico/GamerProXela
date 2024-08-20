from sqlalchemy import Column, Integer,String
from sqlalchemy.orm import declarative_base

from ..db.db  import engine

Base = declarative_base()

class Sucursal (Base):
    __tablename__ = "sucursales"
    id_sucursal = Column (Integer, primary_key = True)
    direccion = Column(String)
    nombre = Column(String)

    Base.metadata.create_all(engine)
