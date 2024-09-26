from fastapi import APIRouter,Depends,HTTPException # type: ignore
from app.db.repository.productoEstanteriaDB import  ProductosEstanteriaDB
from app.models.productoEstanteria import ProdutoEstanteria
from app.models.productoEstanteria import ProductoSearch
from app.db.connection.dependenciesDB import get_connection



router = APIRouter(
    prefix="/produc-rack",
    tags=["productos-estanteria"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (data_producto: ProdutoEstanteria,conn=Depends(get_connection)):
    data = data_producto.dict()
    data.pop("id_estanteria_producto") 
    ProductosEstanteriaDB.insert(conn,data)
    return "los productos de la estateria esta registrados"


@router.delete("delete/{id}")
def delete (id:int,conn=Depends(get_connection)):
        ProductosEstanteriaDB(conn,id)
        return "Producto eliminado"


@router.put("/update/{id}")
def update (data_producto : ProdutoEstanteria, id: int,conn=Depends(get_connection)):
     data = data_producto.dict()
     data ['id_estanteria_producto'] = id
     ProductosEstanteriaDB.update_product(conn,data)
     return "producto actualizado"

@router.get("/list/{id}")
def get_list(id:int,conn=Depends(get_connection)):
      return ProductosEstanteriaDB.list_product(conn,id)

@router.post("/producto-estanteria")
def get_producto (data_producto: ProductoSearch,conn=Depends(get_connection)):
    data= data_producto.dict()
    return ProductosEstanteriaDB.list_product_estanteria(conn,data)
