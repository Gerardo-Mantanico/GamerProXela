from fastapi import FastAPI, HTTPException, status # type: ignore
import psycopg2 # type: ignore
from psycopg2 import OperationalError, DatabaseError # type: ignore
from app.db.connection.database import Database

db = Database()

class SucursalDB:

    # Este metodo se encarga de registrar una sucursal
    def register_branch( data):
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(    """
                            CALL sucursal.insert_sucursal (%(direccion)s, %(nombre)s, %(no_sucursal)s, %(codigo)s, %(correo)s,%(telefono)s,%(horario_apertura)s,%(horario_cierre)s)
                            """,data,
                    )
                conn.commit()
        except (DatabaseError, psycopg2.Error) as e:
            if conn is not None:
                conn.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database operation error")
        
        finally:
                if conn is not None:
                 conn.close()


    # Este metodo se encarga de obtener la informacion de una sucursal
    def see_branch( id):
        with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute( """
                            SELECT * FROM sucursal.sucursal WHERE id_sucursal= %s
                            """,(id,),
                    )
                    return data.fetchone()


    def delete_branch( id):
        with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute( """
                        DELETE FROM sucursal.sucursal WHERE id_sucursal=%s
                        """,(id,),
                    )
                    conn.commit()


    def update_branch( data):
        with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute( """
                            UPDATE sucursal.sucursal
                        	SET  direccion= %(direccion)s , nombre=%(nombre)s, no_sucursal=%(no_sucursal)s
	                        WHERE id_sucursal=%(id_sucursal)s
                            """,data,
                    )
                    conn.commit()

    def branch_list(self):
        with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute( """
                                SELECT * FROM sucursal.sucursal
                                """
                    )
                    return data.fetchall()
