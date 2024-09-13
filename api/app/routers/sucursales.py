from fastapi import APIRouter,HTTPException # type: ignore
from app.db.repository.sucursalDB import SucursalDB
from app.models.sucursales import Sucursal
conn = None


def set_conn(connexion):
    global conn
    conn = connexion
       

router = APIRouter(
    prefix="/branch",
    tags=["sucursales"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (user_data: Sucursal):
     data = user_data.dict() #formater dato
     data.pop("id"); # para quitar el id de la clase
     SucursalDB.register_branch(conn,data)
     print(data)


@router.delete("/delete/{id}")
def delete_branch(id: int):
     data = SucursalDB.delete_branch(conn,id)


@router.get("/{id}")
def get_branch(id:int):
     data = SucursalDB.see_branch(conn,id)
     dictionary = {
            "id": data[0],
            "address": data[1],
            "name": data[2],
            "no_branch": data[3]
     }
     return dictionary


@router.put("/update/{id}")
def update_branch(data_sucursal: Sucursal, id:int): 
     data = data_sucursal.dict()
     data ["id"] = id
     SucursalDB.update_branch(conn,data)


@router.get("/")
def root():
     items = []
     for data in SucursalDB.branch_list(conn):  # Usa `conn.get_connection()` si necesitas obtener la conexión
        dictionary = {
            "id": data[0],
            "address": data[1],
            "name": data[2],
            "no_branch": data[3]
        }
        items.append(dictionary)
     return items
