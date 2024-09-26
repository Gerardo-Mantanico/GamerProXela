from fastapi import APIRouter,Depends,HTTPException # type: ignore
from app.db.repository.productoBodegaDB import ProductoBodegaDB
from app.models.productoBodega import ProductoBodega
from app.db.connection.dependenciesDB import get_connection



router = APIRouter(
    prefix="/product-bodega",
    tags=["productos-bodega"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (product_data: ProductoBodega,conn=Depends(get_connection)):
     data = product_data.dict() #formater dato
     print(data)
     data.pop("id_producto_bodega"); # para quitar el id de la clase
     ProductoBodegaDB.insert_producto(conn,data)


@router.delete("/{id}")
def delete_product(id: int,conn=Depends(get_connection)):
      ProductoBodegaDB.delete_product(conn,id)
      return "producto eliminado de bodega"

@router.get("/{id}")
def get_list(id: int,conn=Depends(get_connection)):
    return  ProductoBodegaDB.product_list(conn,id)

@router.get("/estanteria/{id}")
def get_list(id: int,conn=Depends(get_connection)):
    return  ProductoBodegaDB.product_list_estanteria(conn,id)











