from fastapi import FastAPI, HTTPException, status # type: ignore
import psycopg2 # type: ignore
from psycopg2 import OperationalError, DatabaseError # type: ignore
from app.db.connection.database import Database

db = Database()


class LoginDB():
    def ingresar(data):
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "SELECT * FROM administrador.login(%s, %s)", 
                        (data['email'], data['password'])
                    )
                    result = cur.fetchall() 
                    return result
        except Exception as e:
            print(e)
            conn.rollback();
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database operation error")
