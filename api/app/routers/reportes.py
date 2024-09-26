from fastapi import APIRouter, Depends, HTTPException  # type: ignore
from app.db.repository.reporteDB import ReporteDB
from app.models.fecha import Fecha

router = APIRouter(
    prefix="/reporte",
    tags=["reporte"],
    responses={404: {"description": "Not found"}},
)

@router.post("/historial")
def historial(fecha: Fecha): 
    data = fecha.dict()
    return ReporteDB.historial( data)

@router.post("/top-ventas-grande")
def reportes_ventas_grande(fecha: Fecha): 
    data = fecha.dict()
    return ReporteDB.obtener_top_ventas_grandes( data)

@router.get("/top-sucursales")
def get_top_sucursales(): 
    return ReporteDB.obtener_top_sucursales_ingreso()

@router.get("/top-articulo")
def get_top_articulo(): 
    return ReporteDB.obtener_top_articulos_vendidos()

@router.get("/cliente-gastador")
def get_cliente_gastador(): 
    return ReporteDB.obtener_top_clientes_gastadores()
