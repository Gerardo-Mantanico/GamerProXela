from fastapi import FastAPI, HTTPException, status # type: ignore
import psycopg2 # type: ignore
from psycopg2 import OperationalError, DatabaseError # type: ignore

class SucursalDB:

    # Este metodo se encarga de registrar una sucursal
    def register_branch(self, data):
        try:
             with self.conn.cursor() as cur:
                cur.execute(    """
                            CALL sucursal.insert_sucursal (%(direccion)s, %(nombre)s, %(no_sucursal)s, %(codigo)s, %(correo)s,%(telefono)s,%(horario_apertura)s,%(horario_cierre)s)
                            """,data,
            )
                self.conn.commit()
        except (DatabaseError, psycopg2.Error) as e:
            if self.conn is not None:
                self.conn.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database operation error")
        
        finally:
                if self.conn is not None:
                 self.conn.close()


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
