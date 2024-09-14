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
            "id empleado": credenciales[0][0],
            "id sucursal": credenciales[0][1],
            "rol": credenciales[0][2],
            "dato extra": credenciales[0][3]
     }
    return dictionary
   




