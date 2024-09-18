from fastapi import FastAPI, HTTPException, status # type: ignore
import psycopg2 # type: ignore
from psycopg2 import OperationalError, DatabaseError # type: ignore

class UsuarioDB:

    # Este metodo se encarga de registrar una sucursal
    def register_user(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                """
                            INSERT INTO administrador.empleado(
                            rol, usuario, contrasena, id_sucursal, nombre, telefono, correo)
                            VALUES (%(rol)s, %(usuario)s, %(password)s, %(id_sucursal)s, %(nombre)s, %(telefono)s, %(correo)s)
                            """,
                data,
            )
            self.conn.commit()
        except (DatabaseError, psycopg2.Error) as e:
            self.conn.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database operation error")
        


    def register_empleado(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                """
                            CALL administrador.registrar_empleado( 
                            %(rol)s, %(usuario)s, %(password)s, %(id_sucursal)s, %(nombre)s, %(telefono)s, %(correo)s)
                            """,
                data,
            )
            self.conn.commit()
        except (DatabaseError, psycopg2.Error) as e:
            self.conn.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database operation error")
            

        
    def see_user(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute(
                """
                    SELECT * FROM administrador.empleado WHERE id_empleado=%s
                """,(id,),
            )
            return data.fetchone()
        


    def list_user(self, id):
     with self.conn.cursor() as cur:
        cur.execute(
            """
            SELECT e.id_empleado, e.nombre, e.rol
            FROM administrador.empleado e
            WHERE e.id_sucursal = %s
            """,
            (id,)
        )
        data = cur.fetchall()
        return data




    def delete_user(self, id):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                 DELETE  FROM administrador.empleado WHERE id_empleado=%s
                """,(id,),
            )
            self.conn.commit()    
            
