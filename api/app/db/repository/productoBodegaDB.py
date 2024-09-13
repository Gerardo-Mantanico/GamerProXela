class ProductoBodegaDB():
    def insert_producto(self,data):
        with self.conn.cursor () as cur:
            cur.execute(
                """
                INSERT INTO bodega.producto_bodega(
	            id_bodega, id_producto, cantidad)
	            VALUES (%(id_bodega)s, %(id_producto)s, %(cantidad)s);
                """,data
            )
            self.conn.commit()
    

    def delete_product(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                        DELETE FROM bodega.producto_bodega  WHERE id_producto=%s
                        """,(id,),
            )
            self.conn.commit()


    def update_product(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                            UPDATE bodega.producto_bodega
                        	SET  cantidad=%(cantidad)s
	                        WHERE id_producto_bodega=%(id_producto_bodega)s
                            """,data,
            )
            self.conn.commit()





    def see_producto(self, id):
     with self.conn.cursor() as cur:
        cur.execute("""
            SELECT    categoria FROM bodega.producto WHERE id_producto = %s
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
 
