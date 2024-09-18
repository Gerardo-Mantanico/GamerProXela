class ProductoBodegaDB:
    def insert_producto(self, data):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO bodega.producto_bodega(
	            id_bodega, id_producto, cantidad)
	            VALUES (%(id_bodega)s, %(id_producto)s, %(cantidad)s);
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
             SELECT bc.*, pb.cantidad,pb.id_bodega
             FROM bodega.producto_bodega pb
             INNER JOIN bodega.consola bc ON pb.id_producto = bc.id_producto
             WHERE pb.id_bodega = %s

            """,
                (id_bodega,),
            )
            #resolver el error 
            data = cur.fetchone()
            consola = {
                "id": data[0],
                "codigo": data[1],
                "nombre": data[2],
                "descripcion": data[3],
                "precio": data[4],
                "categoria": "Consola",
                "marca": data[6],
                "modelo": data[7],
                "cantidad": data[8],
                "bodega": data[9],
            }

            # Segunda consulta para Videojuegos
            cur.execute(
                """
                    SELECT  bv.*, pb.cantidad, pb.id_bodega FROM bodega.producto_bodega pb
                    INNER JOIN bodega.videojuego bv ON pb.id_producto = bv.id_producto 
                    WHERE pb.id_bodega = %s
                """,
                (id_bodega,),
            )
            data = cur.cur.fetchall()
            print(data)
            videojuegos = []
            for row in data:
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
                    }
            videojuegos.append(videojuego)

        return {"consola": consola, "videojuego": videojuegos}
