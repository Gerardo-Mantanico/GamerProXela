from fastapi import FastAPI, HTTPException, status  # type: ignore
import psycopg2  # type: ignore
from psycopg2 import OperationalError, DatabaseError  # type: ignore
from app.db.connection.database import Database

db = Database()


class ClienteDB:

    # Este metodo se encarga de registrar una sucursal
    def register_cliente( data):
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                            INSERT INTO cajero.cliente(
                            nombre, nit, telefono, direccion)
                            VALUES ( %(nombre)s, %(nit)s, %(telefono)s, %(direccion)s)
                            RETURNING id_cliente 
                                """,data,
                    )
                    id_cliente = cur.fetchone()[0]
                    conn.commit() 
        except (DatabaseError, psycopg2.Error) as e:
                conn.rollback()
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Database operation error",
                )
        return id_cliente
    

    def see_cliente( nit):
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT * FROM cajero.cliente WHERE nit=%s
                    """,
                    (nit,),
                    )
                    data = cur.fetchone()
                    mapped_data = {
                        "id_cliente": data[0],
                        "nombre": data[1],
                        "nit": data[2].strip(),
                        "telefono": data[3].strip(),
                        "direccion": data[4].strip(),
                    }
                    return mapped_data
        except (DatabaseError, psycopg2.Error) as e:
                conn.rollback()
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database operation error",
            )


    def update_cliente( data):
        print(data)
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                            """
                                UPDATE cajero.cliente
                                SET  nombre=%(nombre)s, telefono=%(telefono)s, direccion=%(direccion)s
                                WHERE nit=%(nit)s
                                    """,
                            data,
                    )
                    conn.commit()
        except (DatabaseError, psycopg2.Error) as e:
            conn.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database operation error",
        )

    def delete_cliente( nit):
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                    DELETE  FROM cajero.cliente WHERE nit=%s
                    """,
                        (nit,),
                    )
                conn.commit()
        except (DatabaseError, psycopg2.Error) as e:
            conn.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database operation error",
            )
