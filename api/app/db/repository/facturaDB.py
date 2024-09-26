from fastapi import FastAPI, HTTPException, status  # type: ignore
import psycopg2  # type: ignore
from psycopg2 import OperationalError, DatabaseError  # type: ignore

from app.db.connection.database import Database
db = Database() 

class FacturaDB:

    # Este metodo se encarga de registrar una sucursal
    def register_facutura( data):
        print(data)
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
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
                conn.commit() 
        except (DatabaseError, psycopg2.Error) as e:
            conn.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database operation error",
            )
        return id_facutura
    

    
    def register_detalles_factura( productos, id_factura):
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
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
                    conn.commit()
        except (DatabaseError, psycopg2.Error) as e:
                conn.rollback()
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Database operation error",
                )


  

    def see_factura( nit):
        with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                            SELECT * FROM cajero.cliente WHERE nit=%s
                        """,
                        (nit,),
                    )
                    return cur.fetchone()

    def update_factura( data):
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

    def delete_factura( nit):
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
