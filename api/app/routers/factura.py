from fastapi import APIRouter,Depends,HTTPException # type: ignore
from app.db.repository.facturaDB import FacturaDB
from app.db.repository.tarjetaDB import TarjetaDB
from app.models.factura import Factura
from app.db.connection.dependenciesDB import get_connection



router = APIRouter(
    prefix="/factura",
    tags=["factura"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (factura_data: Factura,conn=Depends(get_connection)):
     data = factura_data.dict() #formater dato
     productos = data["listProduct"]
     FacturaDB.register_detalles_factura(conn,productos,FacturaDB.register_facutura(conn, data))
     return "factura guardada"


@router.delete("/{id}")
def delete(nit: str,conn=Depends(get_connection)):
      FacturaDB.delete_factura(conn,nit)
      return "cliente eliminado"


@router.put("/{id}")
def update(factura_data: Factura, id: str,conn=Depends(get_connection)):
    print(id)  # Esto debería imprimir el ID en la consola
    data = factura_data.dict()
    data["nit"] = id
    FacturaDB.update_factura(conn, data,conn=Depends(get_connection))
    return {"message": "Cliente actualizado"}

      
@router.get("/{id}")
def get(id:int,conn=Depends(get_connection)):
     return FacturaDB.see_factura(conn,id,)


@router.post("/card/{nit}")
def generetCard(nit: str,conn=Depends(get_connection)):
     return TarjetaDB.generar_tarjeta(conn,nit)




