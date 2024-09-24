from fastapi import FastAPI, HTTPException, status  # type: ignore
import psycopg2  # type: ignore
from psycopg2 import OperationalError, DatabaseError  # type: ignore


class FacturaDB:

    # Este metodo se encarga de registrar una sucursal
    def register_facutura(self, data):
        print(data)
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    """
                        INSERT INTO cajero.factura(
                        id_sucursal, id_cajero, id_cliente, total, descuento_aplicado)
                        VALUES (%(id_sucursal)s, %(id_cajero)s, %(id_cliente)s, %(total)s::money, %(descuento)s::money)
                        RETURNING id_factura; 
                        """,
                    data,
                )
                id_facutura = cur.fetchone()[0]
                self.conn.commit() 
        except (DatabaseError, psycopg2.Error) as e:
            self.conn.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database operation error",
            )
        return id_facutura
    

    
    def register_detalles_factura(self, productos, id_factura):
        try:
            with self.conn.cursor() as cur:
                # Prepara los datos para la inserción
                detalles = [
                    {
                        'id_factura': id_factura,
                        'id_producto': producto['id_producto'],  # Asegúrate de que 'id_producto' existe
                        'cantidad': producto['cantidad'],        # Asegúrate de que 'cantidad' existe
                    }
                    for producto in productos  # Itera sobre la lista de productos
                ]

                # Inserta los detalles en la base de datos
                cur.executemany(
                    """
                    INSERT INTO cajero.detalle_factura (
                        id_factura, id_producto, cantidad)
                    VALUES (%(id_factura)s, %(id_producto)s, %(cantidad)s);
                    """,
                    detalles  # Usa la lista de diccionarios
                )
                self.conn.commit()
        except (DatabaseError, psycopg2.Error) as e:
            self.conn.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database operation error",
            )


  

    def see_factura(self, nit):
        with self.conn.cursor() as cur:
            data = cur.execute(
                """
                    SELECT * FROM cajero.cliente WHERE nit=%s
                """,
                (nit,),
            )
            return data.fetchone()

    def update_factura(self, data):
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

    def delete_factura(self, nit):
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
