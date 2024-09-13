from fastapi import Depends, FastAPI # type: ignore
from app.dependencies import get_query_token, get_token_header
from app.routers import sucursales, productos,usuario,login,productoBodega,bodega,estanteria,estanteriaProducto
from db.connection.db import Connection



conn = Connection()
app = FastAPI()


sucursales.conn=conn;
productos.conn=conn;
usuario.conn=conn;
login.conn=conn;
productoBodega.conn=conn;
bodega.conn = conn;
estanteria.conn = conn;
estanteriaProducto.conn = conn;

app.include_router(sucursales.router)
app.include_router(productos.router)
app.include_router(usuario.router)
app.include_router(login.router)
app.include_router(productoBodega.router)
app.include_router(bodega.router)
app.include_router(estanteria.router)
app.include_router(estanteriaProducto.router)

#uvicorn main:app --host 0.0.0.0 --port 8080  --reload
#export PYTHONPATH=/home/gerardo/Documents/2024/second-semester/files/first-proyect/GamerProXela/api