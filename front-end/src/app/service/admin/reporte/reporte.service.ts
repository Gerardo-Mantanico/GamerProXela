import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ReporteService {

  constructor( private httpClient : HttpClient){ }

  ClienteGastador(){
      return this.httpClient.get<any>("http://0.0.0.0:8080/reporte/cliente-gastador")
  }

  topArticulos(){
     return this.httpClient.get<any>("http://0.0.0.0:8080/reporte/top-articulo")
  }
  
  topSucursal(){
    return this.httpClient.get<any>("http://0.0.0.0:8080/reporte/top-sucursales")
  }
  
  ventasGrandes(fecha: any){
    return this.httpClient.post<any>("http://0.0.0.0:8080/reporte/top-ventas-grande",fecha)
  }

  historial(fecha: any){
    return this.httpClient.post<any>("http://0.0.0.0:8080/reporte/historial",fecha)
  }


}
