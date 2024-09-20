class ProductoBodegaDB:
    def insert_producto(self, data):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                CALL bodega.inser_producto_bodega(%(id_bodega)s, %(id_producto)s, %(cantidad)s)
                """,
                data,
            )
            self.conn.commit()

    def delete_product(self, id):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                        DELETE FROM bodega.producto_bodega  WHERE id_producto=%s
                        """,
                (id,),
            )
            self.conn.commit()

    def update_product(self, data):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                            UPDATE bodega.producto_bodega
                        	SET  cantidad=%(cantidad)s
	                        WHERE id_producto_bodega=%(id_producto_bodega)s
                            """,
                data,
            )
            self.conn.commit()

    def see_producto(self, id):
        with self.conn.cursor() as cur:
            cur.execute(
                """
            SELECT    categoria FROM bodega.producto WHERE id_producto = %s
        """,
                (id,),
            )
            categoria_result = cur.fetchone()

            if categoria_result is None:
                return None

            categoria = categoria_result[0]  # Extrae el valor de la categoría

            # Ejecuta la segunda consulta basada en la categoría
            if categoria == 1:
                cur.execute(
                    """
                SELECT * FROM bodega.consola WHERE id_producto = %s
            """,
                    (id,),
                )
            else:
                cur.execute(
                    """
                SELECT * FROM bodega.videojuego WHERE id_producto = %s
            """,
                    (id,),
                )

            return cur.fetchone()

    def product_list(self, id_bodega):
        with self.conn.cursor() as cur:
            # Primera consulta para Consolas
            cur.execute(
                """
             SELECT bc.*, pb.cantidad,pb.id_bodega,pb.id_producto_bodega
             FROM bodega.producto_bodega pb
             INNER JOIN bodega.consola bc ON pb.id_producto = bc.id_producto
             WHERE pb.id_bodega = %s

            """,
                (id_bodega,),
            )
            #resolver el error 
            data = []
            data = cur.fetchall()
            consolas=[]
            for row in  data:
                consola = {
                    "id": row[0],
                    "codigo": row[1],
                    "nombre": row[2],
                    "descripcion": row[3],
                    "precio": row[4],
                    "categoria": "Consola",
                    "marca": row[6],
                    "modelo": row[7],
                    "cantidad": row[8],
                    "bodega": row[9],
                    "id_producto_bodega" : row [10]
                }
                consolas.append(consola)

            # Segunda consulta para Videojuegos
            cur.execute(
                """
                    SELECT  bv.*, pb.cantidad, pb.id_bodega ,pb.id_producto_bodega
                    FROM bodega.producto_bodega pb
                    INNER JOIN bodega.videojuego bv ON pb.id_producto = bv.id_producto 
                    WHERE pb.id_bodega = %s
                """,
                (id_bodega,),
            )
            data = []
            data = cur.fetchall()
            videojuegos = []
            for row in  data:
                    videojuego = {
                        "id": row[0],
                        "codigo": row[1],
                        "nombre": row[2],
                        "descripcion": row[3],
                        "precio": row[4],
                        "categoria": "Videojuego",
                        "genero": row[6],
                        "fecha_lanzamiento": row[7],
                        "plataforma": row[8],
                        "mecanica": row[9],
                        "cantidad": row[10],
                        "bodega": row[11],
                        "id_producto_bodega" : row [12]
                    }
                    videojuegos.append(videojuego)
        return {"consola": consolas, "videojuego": videojuegos}
