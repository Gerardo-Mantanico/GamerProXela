from fastapi import HTTPException
from ..services.apirouter import router_api
from ..db.db import session
from ..models.productos import Producto, Consola, Videojuego
from ..services import  producto_s

router = router_api("productos")


@router.get("/{id}")
async def get_producto(id: int):    
    producto = producto_s.get_product(session, id)
    return producto
   

@router.get("/")
async def get_productos():
        producto_list = producto_s.get_all_products(session)
        return producto_list


@router.put("/{id}")
async def update_producto(
    id: int, new_codigo: int, new_nombre: str, new_descripcion: str, new_precio: int
):
    query = session.query(Producto).filter(Producto.id_sucursal == id)
    producto = query.first()
    if new_codigo:
        producto.codigo = new_codigo

    elif new_nombre:
        producto = new_nombre

    elif new_descripcion:
        producto.descripcion = new_descripcion

    elif new_precio:
        producto.precio = new_precio

    session.add(producto)
    session.commit()


@router.delete("/{id}")
async def delete_producto(id: int):
    producto = session.query(Producto).filter(Producto.id_producto == id).first()
    session.delete(producto)
    session.commit()
    return {"producto deleted ": producto.nombre}
