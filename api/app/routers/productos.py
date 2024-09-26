from fastapi import APIRouter,HTTPException,Depends # type: ignore
from app.db.repository.productoDB import ProductoDB
from app.models.productos import Videojuegos , Consola
from fastapi import FastAPI, HTTPException, status # type: ignore


router = APIRouter(
    prefix="/product",
    tags=["productos"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (product_data: Consola):
     data = product_data.dict() #formater dato
     data.pop("id"); # para quitar el id de la clase
     categoria = data['categoria']
     ProductoDB.register_product(data,categoria)


@router.get("/{id}")
def get_produc(id:str):
     data = ProductoDB.see_producto( id)
     if data is None:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
     else:
        return data


@router.get("/")
def get_list_product():
     data = ProductoDB.product_list()
     return data


@router.delete("/{id}")
def delete_product(id: int):
      ProductoDB.delete_product(id)
      return "producto eliminado"







