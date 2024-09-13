class SucursalDB:

    # Este metodo se encarga de registrar una sucursal
    def register_branch(self, data):
        with self.conn.cursor() as cur:
            cur.execute(    """
                            INSERT INTO sucursal.sucursal( direccion, nombre, no_sucursal)
                            VALUES (%(direccion)s, %(nombre)s, %(no_sucursal)s)
                            """,data,
            )
            self.conn.commit()

    # Este metodo se encarga de obtener la informacion de una sucursal
    def see_branch(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                            SELECT * FROM sucursal.sucursal WHERE id_sucursal= %s
                            """,(id,),
            )
            return data.fetchone()


    def delete_branch(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                        DELETE FROM sucursal.sucursal WHERE id_sucursal=%s
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

    def branch_list(self):
        with self.conn.cursor() as cur:
            data = cur.execute( """
                                SELECT * FROM sucursal.sucursal
                                """
            )
            return data.fetchall()
