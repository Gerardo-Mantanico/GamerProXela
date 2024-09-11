from fastapi import Depends, FastAPI # type: ignore
from app.dependencies import get_query_token, get_token_header
from app.internal import admin
from app.routers import items, users,sucursales,productos

"""
para resolver el error  export PYTHONPATH=/home/gerardo/Documents/2024/second-semester/files/first-proyect/GamerProXela/api

para agregar un token de acceso
app = FastAPI(dependencies=[Depends(get_query_token)])
"""
app = FastAPI()


app.include_router(users.router)
app.include_router(items.router)
app.include_router(sucursales.router)
app.include_router(productos.router)
"""
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


"""


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}