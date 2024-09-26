from fastapi import APIRouter, Depends, Request, HTTPException # type: ignore
from app.db.repository.loginDB import LoginDB
from app.models.login import Login
from app.db.connection.database import Database

db = Database()

router = APIRouter(
    prefix="/login",
    tags=["login"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (data_login:Login):
    data = data_login.dict() 
    credenciales = LoginDB.ingresar(data)
    print(credenciales)
    dictionary = {
            "id_empleado": credenciales[0][0],
            "id_sucursal": credenciales[0][1],
            "rol": credenciales[0][2],
            "dato_extra": credenciales[0][3],
            "nombre": credenciales[0][4]
     }
    
    if credenciales[0][2]=="C":
        db.connect('cajero', 'cajero2024', 'localhost', 'tu_basedatos')

    elif credenciales[0][2]=='B':
       db.connect('bodega', 'bodega2024', 'localhost', 'tu_basedatos')

    elif credenciales[0][2]=='I':
        db.connect('inventario', 'inventario2024', 'localhost', 'tu_basedatos')
        

    elif credenciales[0][2]=='A':
        db.connect('admin', 'admin2024', 'localhost', 'tu_basedatos')


    return dictionary
   




