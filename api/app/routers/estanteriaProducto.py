from fastapi import APIRouter,HTTPException # type: ignore
from app.db.repository.productoEstanteriaDB import  ProductosEstanteriaDB
from app.models.productoEstanteria import ProdutoEstanteria
conn = None



router = APIRouter(
    prefix="/produc-rack",
    tags=["productos-estanteria"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (data_producto: ProdutoEstanteria):
    data = data_producto.dict()
    data.pop("id_estanteria_producto") 
    ProductosEstanteriaDB.insert(conn,data)
    return "los productos de la estateria esta registrados"


@router.delete("delete/{id}")
def delete (id:int):
        ProductosEstanteriaDB(conn,id)
        return "Producto eliminado"


@router.put("/update/{id}")
def update (data_producto : ProdutoEstanteria, id: int):
     data = data_producto.dict()
     data ['id_estanteria_producto'] = id
     ProductosEstanteriaDB.update_product(conn,data)
     return "producto actualizado"

@router.get("/list/{id}")
def get_list(id:int):
      return ProductosEstanteriaDB.list_product(conn,id)