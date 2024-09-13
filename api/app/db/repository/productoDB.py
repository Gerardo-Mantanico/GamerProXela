class ProductoDB:

    # Este metodo se encarga de registrar una sucursal
    def register_product(self, data, type):
        with self.conn.cursor() as cur:

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
                 
            self.conn.commit()

    def see_producto(self, id):
     with self.conn.cursor() as cur:
        cur.execute("""
            SELECT categoria FROM bodega.producto WHERE id_producto = %s
        """, (id,))
        categoria_result = cur.fetchone()

        if categoria_result is None:
            return None
        
        categoria = categoria_result[0]  # Extrae el valor de la categoría

        # Ejecuta la segunda consulta basada en la categoría
        if categoria == 1:
            cur.execute("""
                SELECT * FROM bodega.consola WHERE id_producto = %s
            """, (id,))
        else:
            cur.execute("""
                SELECT * FROM bodega.videojuego WHERE id_producto = %s
            """, (id,))

        return cur.fetchone()



    def delete_product(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                        DELETE FROM bodega.producto  WHERE id_producto=%s
                        """,(id,),
            )
            self.conn.commit()


    def update_branch(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                            UPDATE sucursal.sucursal
                        	SET  direccion= %(direccion)s , nombre=%(nombre)s, no_sucursal=%(no_sucursal)s
	                        WHERE id_sucursal=%(id_sucursal)s
                            """,data,
            )
            self.conn.commit()




    def product_list(self):
        with self.conn.cursor() as cur:
            cur.execute( """
                                 SELECT * FROM bodega.consola
                                """
            )
            consola = cur.fetchall()
        with self.conn.cursor() as cur:
                cur.execute( """
                                SELECT * FROM bodega.videojuego
                                """
            )   
                videojuego=cur.fetchall() 
    
        return {
            'consola': consola,
            'videojuego': videojuego
    }
        