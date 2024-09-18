from fastapi import APIRouter,HTTPException # type: ignore
from app.db.repository.loginDB import LoginDB
from app.models.login import Login
conn = None



router = APIRouter(
    prefix="/login",
    tags=["login"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (data_login: Login):
    data = data_login.dict()
    print(data) 
    credenciales=LoginDB.ingresar(conn,data)
  
    dictionary = {
            "id_empleado": credenciales[0][0],
            "id_sucursal": credenciales[0][1],
            "rol": credenciales[0][2],
            "dato_extra": credenciales[0][3],
            "nombre": credenciales[0][4]
     }
    return dictionary
   




