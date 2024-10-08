from fastapi import APIRouter,Depends,HTTPException # type: ignore
from app.db.repository.productoEstanteriaDB import  ProductosEstanteriaDB
from app.models.productoEstanteria import ProdutoEstanteria
from app.models.productoEstanteria import ProductoSearch



router = APIRouter(
    prefix="/produc-rack",
    tags=["productos-estanteria"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (data_producto: ProdutoEstanteria):
    data = data_producto.dict()
    data.pop("id_estanteria_producto") 
    ProductosEstanteriaDB.insert(data)
    return "los productos de la estateria esta registrados"


@router.delete("delete/{id}")
def delete (id:int):
        ProductosEstanteriaDB(id)
        return "Producto eliminado"


@router.put("/update/{id}")
def update (data_producto : ProdutoEstanteria, id: int):
     data = data_producto.dict()
     data ['id_estanteria_producto'] = id
     ProductosEstanteriaDB.update_product(data)
     return "producto actualizado"

@router.get("/list/{id}")
def get_list(id:int):
      return ProductosEstanteriaDB.list_product(id)

@router.post("/producto-estanteria")
def get_producto (data_producto: ProductoSearch):
    data= data_producto.dict()
    return ProductosEstanteriaDB.list_product_estanteria(data)
