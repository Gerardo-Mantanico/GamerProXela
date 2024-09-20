class ProductosEstanteriaDB():
     
    def insert(self, data):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO inventario.estanteria_producto(
	            id_estanteria, id_producto_bodega, no_pasillo, cantidad)
	            VALUES ( %(id_estanteria)s, %(id_producto_bodega)s, %(no_pasillo)s, %(cantidad)s)
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

    def list_product(self, id):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                    SELECT  * from inventario.productos_estanteria where id_estanteria=%s
                """,(id,)
            )
            data = []
            data = cur.fetchall()
            productos = []
            for row in  data:
                    producto = {
                        "id_producto_estanteria": row[0],
                        "id_producto": row[5],
                        "codigo": row[6],
                        "nombre": row[7],
                        "descripcion": row[8],
                        "precio": row[9],
                        "categoria": row[10],
                        "no_pasillo": row[3],
                        "existencia": row[4],
                    }
                    productos.append(producto)
        return {"productos": productos}
    

        
    
