from fastapi import APIRouter,HTTPException # type: ignore
from app.db.repository.bodegaDB import BodegaDB
from app.models.bodega import Bodega
conn = None



router = APIRouter(
    prefix="/bodega",
    tags=["bodegas"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (data_bodega: Bodega):
    data = data_bodega.dict()
    data.pop("id_bodega") 
    BodegaDB.insert(conn,data)
    return "bodega registrada"


@router.delete("delete/{id}")
def delete (id:int):
        BodegaDB.delete(conn,id)
        return "bodega eliminada"


@router.put("/update/{id}")
def update (data_bodega : Bodega, id: int):
     data = data_bodega.dict()
     data ['id_bodega'] = id
     BodegaDB.update(conn, data)
     return "bodega actualizada"



