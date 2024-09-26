from fastapi import APIRouter,Depends,HTTPException # type: ignore
from app.db.repository.clienteDB import ClienteDB
from app.models.cliente import Cliente



router = APIRouter(
    prefix="/cliente",
    tags=["cliente"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (cliente_data: Cliente):
     data = cliente_data.dict() #formater dato
     data.pop("id_cliente"); # para quitar el id de la clase
     return {"id_cliente": ClienteDB.register_cliente( data)}


@router.delete("/{id}")
def delete(nit: str):
      ClienteDB.delete_cliente(nit)
      return "cliente eliminado"


@router.put("/{id}")
def update(cliente_data: Cliente, id: str):
    print(id)  # Esto debería imprimir el ID en la consola
    data = cliente_data.dict()
    data["nit"] = id
    ClienteDB.update_cliente( data)
    return {"message": "Cliente actualizado"}

      
@router.get("/{nit}")
def get(nit:str):
     return ClienteDB.see_cliente(nit) 




