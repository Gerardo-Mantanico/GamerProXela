from fastapi import APIRouter,HTTPException # type: ignore
from app.db.repository.productoBodegaDB import ProductoBodegaDB
from app.models.productoBodega import ProductoBodega
conn = None



router = APIRouter(
    prefix="/product-bodega",
    tags=["productos-bodega"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (product_data: ProductoBodega):
     data = product_data.dict() #formater dato
     print(data)
     data.pop("id_producto_bodega"); # para quitar el id de la clase
     ProductoBodegaDB.insert_producto(conn,data)


@router.delete("/{id}")
def delete_product(id: int):
      ProductoBodegaDB.delete_product(conn,id)
      return "producto eliminado de bodega"

@router.get("/{id}")
def get_list(id: int):
    return  ProductoBodegaDB.product_list(conn,id)











