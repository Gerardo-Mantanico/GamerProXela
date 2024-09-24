from fastapi import FastAPI, HTTPException, status  # type: ignore
import psycopg2  # type: ignore
from psycopg2 import OperationalError, DatabaseError  # type: ignore


class FacturaDB:

    # Este metodo se encarga de registrar una sucursal
    def register_facutura(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    """
                        INSERT INTO cajero.cliente(
	                    nombre, nit, telefono, direccion)
	                    VALUES ( %(nombre)s, %(nit)s, %(telefono)s, %(direccion)s);
                            """,
                    data,
                )
            self.conn.commit()
        except (DatabaseError, psycopg2.Error) as e:
            self.conn.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database operation error",
            )

    def see_cliente(self, nit):
        with self.conn.cursor() as cur:
            data = cur.execute(
                """
                    SELECT * FROM cajero.cliente WHERE nit=%s
                """,
                (nit,),
            )
            return data.fetchone()

    def update_cliente(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    """
                            
                        UPDATE cajero.cliente
                        SET  nombre=%(nombre)s, telefono=%(telefono)s, direccion=%(direccion)s
                        WHERE nit=%(nit)s
                            """,
                    data,
                )
            self.conn.commit()
        except (DatabaseError, psycopg2.Error) as e:
            self.conn.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database operation error",
            )

    def delete_user(self, nit):
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    """
                 DELETE  FROM cajero.cliente WHERE nit=%s
                """,
                    (nit,),
                )
            self.conn.commit()
        except (DatabaseError, psycopg2.Error) as e:
            self.conn.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database operation error",
            )
