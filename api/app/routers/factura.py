from fastapi import APIRouter,Depends,HTTPException # type: ignore
from app.db.repository.facturaDB import FacturaDB
from app.db.repository.tarjetaDB import TarjetaDB
from app.models.factura import Factura




router = APIRouter(
    prefix="/factura",
    tags=["factura"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (factura_data: Factura):
     data = factura_data.dict() #formater dato
     productos = data["listProduct"]
     FacturaDB.register_detalles_factura(productos,FacturaDB.register_facutura( data))
     return "factura guardada"


@router.delete("/{id}")
def delete(nit: str):
      FacturaDB.delete_factura(nit)
      return "cliente eliminado"


@router.put("/{id}")
def update(factura_data: Factura, id: str):
    print(id)  # Esto debería imprimir el ID en la consola
    data = factura_data.dict()
    data["nit"] = id
    FacturaDB.update_factura( data)
    return {"message": "Cliente actualizado"}

      
@router.get("/{id}")
def get(id:int):
     return FacturaDB.see_factura(id,)


@router.post("/card/{nit}")
def generetCard(nit: str):
     return TarjetaDB.generar_tarjeta(nit)




