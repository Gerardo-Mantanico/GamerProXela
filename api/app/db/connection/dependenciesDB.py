# app/dependencies.py
from fastapi import Depends, HTTPException # type: ignore
from db.connection.db import Connection

conn = Connection()

def get_connection():
    return conn
