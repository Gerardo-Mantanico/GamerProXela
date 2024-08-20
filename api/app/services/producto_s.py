from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.productos import Producto, Consola, Videojuego


# metodo para obtener un producto mediante el id
def get_product(session, id):
    producto = session.query(Producto).filter(Producto.id_producto == id).first()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")

    # Crear el diccionario base con la información común
    product_data = {
        "id_producto": producto.id_producto,
        "codigo": producto.codigo,
        "nombre": producto.nombre,
        "descripcion": producto.descripcion,
        "precio": producto.precio,
    }

    # Añadir información específica basada en la categoría
    if producto.categoria.strip().lower() == "consola":
        consola = (
            session.query(Consola)
            .filter(Consola.id_producto == producto.id_producto)
            .first()
        )
        if consola is None:
            raise HTTPException(status_code=404, detail="Consola not found")
        product_data["consola"] = {"marca": consola.marca, "modelo": consola.modelo}

    elif producto.categoria.strip().lower() == "videojuegos":
        videojuego = (
            session.query(Videojuego)
            .filter(Videojuego.id_producto == producto.id_producto)
            .first()
        )
        if videojuego is None:
            raise HTTPException(status_code=404, detail="Videojuego not found")
        product_data["videojuego"] = {
            "genero": videojuego.genero,
            "año_lanzamiento": videojuego.ano_lanzamiento,
            "plataforma": videojuego.plataforma,
            "mecanica": videojuego.mecanica,
        }

    else:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown product category: {producto.categoria.strip()}",
        )

    return product_data


# metodo para obtener  la lista de productos
def get_all_products(session):
    productos = session.query(Producto).all()
    if not productos:
        raise HTTPException(status_code=404, detail="No products found")

    product_list = []
    for producto in productos:
        product_data = {
            "id_producto": producto.id_producto,
            "codigo": producto.codigo,
            "nombre": producto.nombre,
            "descripcion": producto.descripcion,
            "precio": producto.precio,
        }

        if producto.categoria.strip().lower() == "consola":
            consola = (
                session.query(Consola)
                .filter(Consola.id_producto == producto.id_producto)
                .first()
            )
            if consola:
                product_data["consola"] = {
                    "marca": consola.marca,
                    "modelo": consola.modelo,
                }

        elif producto.categoria.strip().lower() == "videojuegos":
            videojuego = (
                session.query(Videojuego)
                .filter(Videojuego.id_producto == producto.id_producto)
                .first()
            )
            if videojuego:
                product_data["videojuego"] = {
                    "genero": videojuego.genero,
                    "ano_lanzamiento": videojuego.ano_lanzamiento,
                    "plataforma": videojuego.plataforma,
                    "mecanica": videojuego.mecanica,
                }

        product_list.append(product_data)

    return product_list
