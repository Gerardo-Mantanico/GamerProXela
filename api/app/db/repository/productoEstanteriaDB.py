from app.db.connection.database import Database
db = Database()


class ProductosEstanteriaDB():
     
    def insert(data):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CALL inventario.insertar_productos_estanteria(%(id_estanteria)s, %(id_producto)s, %(cantidad)s, %(id_pasillo)s)
                    """,data,
                )
                conn.commit()


    def delete( id):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                        DELETE FROM inventario.estanteria_producto  WHERE id_estanteria_producto=%s
                        """,
                    (id,),
                )
                conn.commit()


    def update_product( data):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                        UPDATE inventario.estanteria_producto
	                    SET  id_estanteria=%(id_estanteria)s, id_producto_bodega=%(id_producto_bodega)s, no_pasillo=%(no_pasillo)s
	                    WHERE id_estanteria_producto=%(id_estanteria_producto)s
                            """,
                    data,
                )
                conn.commit()



    def list_product( id):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                        SELECT *  FROM inventario.producto_estanteria WHERE id_estanteria=%s
                    """,(id,)
                )
                data = []
                data = cur.fetchall()
                productos = []
                for row in  data:
                    categoria = "Videojuego" if data[6] == 1 else "Consola"
                    producto = {
                        "id_producto_estanteria": row[0],
                        "id_producto": row[1],
                        "codigo": row[2],
                        "nombre": row[3],
                        "descripcion": row[4],
                        "precio": row[5],
                        "categoria": categoria,
                        "no_pasillo": row[8],
                        "descripcion_pasillo": row[9],
                        "existencia": row[7],
                    }
                    productos.append(producto)
                return {"productos": productos}
            

    

    def list_product_estanteria(data):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT * 
                    FROM inventario.producto_estanteria 
                    WHERE id_sucursal = %(id_sucursal)s 
                    AND (LOWER(codigo_producto) = LOWER(%(codigo_producto)s) 
                    OR LOWER(nombre) = LOWER(%(nombre)s))
                    """, data,
                )

                product_data = cur.fetchone()

                if product_data:
                    categoria = "Consola" if product_data[6] == 1 else "Videojuego"
                    mapped_data = {
                        "id_productoEstanteria": product_data[0],
                        "id_producto": product_data[1],
                        "codigo": product_data[2].strip(),  # Eliminar espacios en blanco
                        "nombre": product_data[3].strip(),
                        "descripcion": product_data[4].strip(),
                        "precio": product_data[5].strip(),
                        "categoria": categoria,
                        "existencia": product_data[7],
                        "no_pasillo": product_data[8],
                        "descripcion_pasillo": product_data[9],
                    }
                    return mapped_data
                else:
                    
                    return None  

        
        
    
    
        
    

    

        
    
          