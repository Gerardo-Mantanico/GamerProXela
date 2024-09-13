class EstanteriaDB:
    def insert(self, data):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO inventario.estanteria(
            	id_sucursal, id_empleado)
            	VALUES ( %(id_sucursal)s , %(id_empleado)s);
                """,
                data,
            )
            self.conn.commit()


    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute(
            """
                        DELETE FROM inventario.estanteria  WHERE id_estanteria=%s
                        """,
            (id,),
        )
        self.conn.commit()


    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute(
            """
                        UPDATE inventario.estanteria
	                    SET  id_sucursal=%(id_sucursal)s, id_empleado=%(id_empleado)s
	                    WHERE id_estanteria=%(id_estanteria)s
                            """,
            data,
        )
        self.conn.commit()
