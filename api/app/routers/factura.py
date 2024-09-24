from fastapi import APIRouter,HTTPException # type: ignore
from app.db.repository.facturaDB import FacturaDB
from app.models.factura import Factura
conn = None



router = APIRouter(
    prefix="/factura",
    tags=["factura"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (factura_data: Factura):
     data = factura_data.dict() #formater dato
     productos = data["listProduct"]
     FacturaDB.register_detalles_factura(conn,productos,FacturaDB.register_facutura(conn, data))
     return "factura guardada"


@router.delete("/{id}")
def delete(nit: str):
      FacturaDB.delete_factura(conn,nit)
      return "cliente eliminado"


@router.put("/{id}")
def update(factura_data: Factura, id: str):
    print(id)  # Esto debería imprimir el ID en la consola
    data = factura_data.dict()
    data["nit"] = id
    FacturaDB.update_factura(conn, data)
    return {"message": "Cliente actualizado"}

      
@router.get("/{id}")
def get(id:int):
     return FacturaDB.see_factura(conn,id)




