from fastapi import APIRouter,Depends,HTTPException # type: ignore
from app.db.repository.usuarioDB import  UsuarioDB
from app.models.usuario import Usuario, Cajero
from app.db.connection.dependenciesDB import get_connection


router = APIRouter(
    prefix="/user",
    tags=["Usuarios"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (user_data: Usuario,conn=Depends(get_connection) ):
     data = user_data.dict() #formater dato
     data.pop("id"); # para quitar el id de la clase
     UsuarioDB.register_user(  conn ,data)


@router.post("/cashier")
def insert(user_data : Usuario,conn=Depends(get_connection) ):
        data = user_data.dict()
        data.pop("id")
        UsuarioDB.register_empleado(conn, data)

@router.get("/{id}")
def get_user(id:int,conn=Depends(get_connection) ):
    return UsuarioDB.see_user(conn,id) 


@router.get("/users/{id}")
def get_users(id: int,conn=Depends(get_connection) ):
    items = []
    for data in UsuarioDB.list_user(conn, id): 
        dictionary = {
            "id_empleado": data[0],
            "nombre": data[1],
            "rol": data[2],
        }
        items.append(dictionary)
    return items




 
@router.delete("/delete/{id}")
def delete_user(id: int,conn=Depends(get_connection) ):
      UsuarioDB.delete_user(conn,id)
      return "Usuario eliminado" 



