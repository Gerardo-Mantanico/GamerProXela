class BodegaDB():
    
    def insert(self, data):
        with self.conn.cursor() as cur:
            cur.execute(    """
                            INSERT INTO bodega.bodega (id_empleado, id_sucursal) 
                            VALUES (%(id_empleado)s  ,%(id_sucursal)s);
                            """,data,
            )
            self.conn.commit()



    def delete (self, id):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                    DELETE FROM bodega.bodega WHERE id_bodega=%s
                """,(id,)
            )
            self.conn.commit()

    def update(self,data):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                    UPDATE bodega.bodega SET id_empleado=%(id_empleado)s, id_sucursal=%(id_sucursal)s
                    WHERE id_bodega=%(id_bodega)s
                """,data
            )
            self.conn.commit();
                  