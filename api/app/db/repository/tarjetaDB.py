from fastapi import FastAPI, HTTPException, status  # type: ignore
import psycopg2  # type: ignore
from psycopg2 import OperationalError, DatabaseError  # type: ignore


class TarjetaDB:
    def generar_tarjeta(self, nit):
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    """
                        INSERT INTO cajero.tarjeta(
                        id_cliente, tipo_tarjeta, puntos)
                        VALUES ( (select id_cliente from cajero.cliente where nit=%(nit)s), 'Común', 0);
                    """,
                    {'nit': nit},  # Pass a dictionary here
                )

                self.conn.commit() 
        except (DatabaseError, psycopg2.Error) as e:
            self.conn.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database operation error",
            )
        return True


    def see_cliente(self, nit):
        with self.conn.cursor() as cur:
            try:    
                cur.execute(
                    """
                    SELECT * FROM cajero.tarjeta WHERE id_cliente=%s
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
                self.conn.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database operation error",
            )


    def update_cliente(self, data):
        print(data)
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    """
                        UPDATE cajero.tarjeta
                        SET id_tarjeta=?, id_cliente=?, tipo_tarjeta=?, puntos=?, fecha_emision=?
                        WHERE id_cliente=%(id_cliente)s;

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