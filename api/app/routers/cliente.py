from fastapi import APIRouter,HTTPException # type: ignore
from app.db.repository.clienteDB import ClienteDB
from app.models.cliente import Cliente
conn = None



router = APIRouter(
    prefix="/cliente",
    tags=["cliente"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (cliente_data: Cliente):
     data = cliente_data.dict() #formater dato
     data.pop("id_cliente"); # para quitar el id de la clase
     ClienteDB.register_cliente(conn, data)
     return "Cliente registrado"


@router.delete("/{id}")
def delete(nit: str):
      ClienteDB.delete_cliente(conn,nit)
      return "cliente eliminado"


@router.put("/{id}")
def update(cliente_data: Cliente, id: str):
    print(id)  # Esto debería imprimir el ID en la consola
    data = cliente_data.dict()
    data["nit"] = id
    ClienteDB.update_cliente(conn, data)
    return {"message": "Cliente actualizado"}

      
@router.get("/{nit}")
def get(nit:str):
     return ClienteDB.see_cliente(conn,nit) 




