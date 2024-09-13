from fastapi import APIRouter,HTTPException # type: ignore
from app.db.repository.estanteriaDB import EstanteriaDB
from app.models.estanteria import Estanteria
conn = None



router = APIRouter(
    prefix="/estanteria",
    tags=["estanteria"],
    responses={404: {"description": "Not found"}},
)


@router.post("/insert")
def insert (estanteria_data: Estanteria):
     data = estanteria_data.dict() #formater dato
     data.pop("id_estanteria"); # para quitar el id de la clase
     EstanteriaDB.insert(conn,data)
     return "Estateria registrada"


@router.delete("/{id}")
def delete_product(id: int):
      EstanteriaDB.delete(conn,id)
      return "estanteria eliminado"


@router.put("/id")
def update(estateria_data: Estanteria, id:int):
      data=estateria_data.dict()
      data["id_estanteria"] =id
      EstanteriaDB.update(conn,data)
      return "Estanteria registrada"
      






