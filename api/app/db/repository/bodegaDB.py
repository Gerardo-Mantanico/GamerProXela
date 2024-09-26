from app.db.connection.database import Database
db = Database()

class BodegaDB():
    
    def insert( data):
        with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(   """
                                    INSERT INTO bodega.bodega (id_empleado, id_sucursal) 
                                    VALUES (%(id_empleado)s  ,%(id_sucursal)s);
                                    """,data,
                    )
                    conn.commit()



    def delete ( id):
        with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                            DELETE FROM bodega.bodega WHERE id_bodega=%s
                        """,(id,)
                    )
                    conn.commit()

    def update(data):
        with db.get_connection() as conn:
                with conn.cursor() as cur:
                        cur.execute(
                    """
                        UPDATE bodega.bodega SET id_empleado=%(id_empleado)s, id_sucursal=%(id_sucursal)s
                        WHERE id_bodega=%(id_bodega)s
                    """,data
                )
                conn.commit();
                    