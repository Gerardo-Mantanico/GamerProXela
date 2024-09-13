class ProductosEstanteriaDB():
     
    def insert(self, data):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO inventario.estanteria_producto(
	            id_estanteria, id_producto_bodega, no_pasillo)
	            VALUES ( %(id_estanteria)s, %(id_producto_bodega)s, %(no_pasillo)s)
                """,data,
            )
            self.conn.commit()


    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute(
            """
                        DELETE FROM inventario.estanteria_producto  WHERE id_estanteria_producto=%s
                        """,
            (id,),
        )
        self.conn.commit()


    def update_product(self, data):
        with self.conn.cursor() as cur:
            cur.execute(
            """
                        UPDATE inventario.estanteria_producto
	                    SET  id_estanteria=%(id_estanteria)s, id_producto_bodega=%(id_producto_bodega)s, no_pasillo=%(no_pasillo)s
	                    WHERE id_estanteria_producto=%(id_estanteria_producto)s
                            """,
            data,
        )
        self.conn.commit()

        
    
