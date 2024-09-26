from app.db.connection.database import Database

db = Database()


class EstanteriaDB:
    def insert( data):
        with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO inventario.estanteria(
                        id_sucursal, id_empleado)
                        VALUES ( %(id_sucursal)s , %(id_empleado)s);
                        """,
                        data,
                    )
                    conn.commit()


    def delete( id):
        with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                                    DELETE FROM inventario.estanteria  WHERE id_estanteria=%s
                                    """,
                        (id,),
                    )
                    conn.commit()


    def update( data):
        with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                                    UPDATE inventario.estanteria
                                    SET  id_sucursal=%(id_sucursal)s, id_empleado=%(id_empleado)s
                                    WHERE id_estanteria=%(id_estanteria)s
                                        """,
                        data,
                    )
                    conn.commit()


    
    def no_pasillo( id):
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT numero, descripcion, id_pasillo FROM  inventario.pasillo WHERE id_sucursal=%s", (id,))
                    data = []
                    data = cur.fetchall()
                    pasillos = []
                    for row in  data:
                        pasillo = {
                            "no": row[0],
                            "descripcion": row[1],
                            "id_pasillo": row[2]
                        
                        }
                        pasillos.append(pasillo)
                    return {"pasillo": pasillos}
        except Exception as e:
                conn.rollback()  # revertir la transacción
                raise e    


