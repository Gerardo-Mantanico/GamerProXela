from fastapi import APIRouter, Depends, HTTPException  # type: ignore
from app.db.repository.reporteDB import ReporteDB
from app.models.fecha import Fecha
from app.db.connection.dependenciesDB import get_connection

router = APIRouter(
    prefix="/reporte",
    tags=["reporte"],
    responses={404: {"description": "Not found"}},
)

@router.post("/historial")
def historial(fecha: Fecha, conn=Depends(get_connection)): 
    data = fecha.dict()
    return ReporteDB.historial(conn, data)

@router.post("/top-ventas-grande")
def reportes_ventas_grande(fecha: Fecha, conn=Depends(get_connection)): 
    data = fecha.dict()
    return ReporteDB.obtener_top_ventas_grandes(conn, data)

@router.get("/top-sucursales")
def get_top_sucursales(conn=Depends(get_connection)): 
    return ReporteDB.obtener_top_sucursales_ingreso(conn)

@router.get("/top-articulo")
def get_top_articulo(conn=Depends(get_connection)): 
    return ReporteDB.obtener_top_articulos_vendidos(conn)

@router.get("/cliente-gastador")
def get_cliente_gastador(conn=Depends(get_connection)): 
    return ReporteDB.obtener_top_clientes_gastadores(conn)
