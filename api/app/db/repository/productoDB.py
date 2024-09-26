from app.db.connection.database import Database

db = Database()

class ProductoDB:

    # Este metodo se encarga de registrar una sucursal
    def register_product( data, type):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                if type==1:
                    cur.execute(    """
                                INSERT INTO bodega.consola(
                                codigo_producto, nombre, descrpcion, precio, categoria, marca, modelo)
                                VALUES (%(codigo)s,%(nombre)s, %(descripcion)s, %(precio)s::money, %(categoria)s, %(marca)s, %(modelo)s)
                                """,data,
                    )

                else:
                    cur.execute(    """
                                INSERT INTO bodega.videojuego(
                                codigo_producto, nombre, descrpcion, precio, categoria, genero, fecha_lanzamiento, plataforma, mecanica)
                                VALUES (%(codigo)s,%(nombre)s, %(descripcion)s, %(precio)s::money, %(categoria)s, %(genero)s, %(fecha_lanzamiento)s,
                                %(plataforma)s, %(mecanica)s)
                                """,data,
                    )
                    
                conn.commit()

    def see_producto( id):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT categoria FROM bodega.producto WHERE codigo_producto = %s
                    """, (id,))
                categoria_result = cur.fetchone()

                if categoria_result is None:
                    return None
                
                categoria = categoria_result[0]  

                # Ejecuta la segunda consulta basada en la categoría
                if categoria == 1:
                    cur.execute("""
                        SELECT * FROM bodega.consola WHERE codigo_producto = %s
                    """, (id,))
                    data= cur.fetchone()

                    dictionary = {
                    "id": data[0],
                    "codigo": data[1],
                    "nombre": data[2],
                    "descripcion": data[3],
                    "precio": data[4],
                    "categoria": "Consola",
                    "marca": data[6],
                    "modelo":  data[7]
                }


                else:
                    cur.execute("""
                        SELECT * FROM bodega.videojuego WHERE codigo_producto = %s
                    """, (id,))
                    data= cur.fetchone()
                    dictionary = {
                    "id": data[0],
                    "codigo": data[1],
                    "nombre": data[2],
                    "descripcion": data[3],
                    "precio": data[4],
                    "categoria": "Videojuego",
                    "genero": data[6],
                    "fecha_lanzamiento":  data[7],
                    "plataforma": data[8],
                    "mecanica": data[9]
                }

                return dictionary



    def delete_product( id):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                        DELETE FROM bodega.producto  WHERE id_producto=%s
                        """,(id,),
                )
                conn.commit()


    def update_branch( data):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                            UPDATE sucursal.sucursal
                        	SET  direccion= %(direccion)s , nombre=%(nombre)s, no_sucursal=%(no_sucursal)s
	                        WHERE id_sucursal=%(id_sucursal)s
                            """,data,
                )
                conn.commit()




    def product_list(self):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute( """
                    SELECT * FROM bodega.consola
                    """
                )
                consola = cur.fetchall()
                
        with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        ELECT * FROM bodega.videojuego
                                """
                    )   
                    videojuego=cur.fetchall() 
    
        return {
            'consola': consola,
            'videojuego': videojuego
    }
        