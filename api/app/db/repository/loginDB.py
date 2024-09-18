from fastapi import FastAPI, HTTPException, status # type: ignore
import psycopg2 # type: ignore
from psycopg2 import OperationalError, DatabaseError # type: ignore

class LoginDB():

   def ingresar(self, data):

        try:   
            with self.conn.cursor() as cur:
                # Ejecutar la función almacenada y pasar parámetros de forma segura
                cur.execute(
                    "SELECT * FROM administrador.login(%s, %s)", 
                    (data['email'], data['password'])
                )
                # Obtener todos los resultados
                data = cur.fetchall()
                return data
        except Exception as e:
                print(e)
                self.conn.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database operation error")
     
        