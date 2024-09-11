from sqlalchemy.orm import declarative_base, relationship # type: ignore
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date # type: ignore
from ..db.db  import engine
Base = declarative_base()

class Producto(Base):
    __tablename__ = "productos";
    __table_args__ = {'schema': 'bodega'}  # Especifica el esquema 
    id_producto = Column(Integer, primary_key=True)
    codigo = Column(Integer, unique=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text)
    precio = Column(String)
    categoria = Column(String)


class Consola(Base):
    __tablename__ = "consola"
    __table_args__ = {'schema': 'bodega'}  # Especifica el esquema 
    id_producto = Column(Integer, ForeignKey('productos.id_producto'), primary_key=True)
    marca = Column(String)
    modelo = Column(String)


class Videojuego(Base):
    __tablename__ = "videojuegos"
    __table_args__ = {'schema': 'bodega'}  # Especifica el esquema 
    id_producto = Column(Integer, ForeignKey('productos.id_producto'), primary_key=True)
    genero = Column(String)
    ano_lanzamiento = Column(Date)
    plataforma = Column(String)
    mecanica = Column(String)

    Base.metadata.create_all(engine)
