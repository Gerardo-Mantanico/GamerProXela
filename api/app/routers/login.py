from fastapi import APIRouter,HTTPException # type: ignore
from app.db.repository.loginDB import LoginDB
from app.models.login import Login
from app.db.connection.dependenciesDB  import get_connection,conn
from app.db.connection.dbCajero import  ConnectionCajero
from app.db.connection.dbBodega import  ConnectionBodega
from app.db.connection.dbInventario import  ConnectionInventario
from app.db.connection.dbAdministrador  import  ConnectionAdmin



router = APIRouter(
    prefix="/login",
    tags=["login"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (data_login: Login):
    data = data_login.dict() 
    global conn
    credenciales=LoginDB.ingresar(get_connection(),data)
    dictionary = {
            "id_empleado": credenciales[0][0],
            "id_sucursal": credenciales[0][1],
            "rol": credenciales[0][2],
            "dato_extra": credenciales[0][3],
            "nombre": credenciales[0][4]
     }
    if credenciales[0][2]=="C":
        conn= ConnectionCajero

    elif credenciales[0][2]=='B':
        conn= ConnectionBodega

    elif credenciales[0][2]=='I':
        conn= ConnectionInventario

    elif credenciales[0][2]=='A':
        conn= ConnectionAdmin

    return dictionary
   




