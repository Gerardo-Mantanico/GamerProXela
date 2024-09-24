import { Injectable } from '@angular/core';
import { ProductoFactura } from '../../model/productoFactura';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class FacturaService {

  private listProductos: ProductoFactura[] = [];
  private total!: number
  private urlCliente="http://0.0.0.0:8080/cliente"

  constructor(private httpClient: HttpClient) { }

  setListProductos(listProductos: ProductoFactura[] = []){
    this.listProductos= listProductos;
  }

  getListaProductos(){
    return this.listProductos
  }

  getTotal(){
    return this.total;
  }
  setTotal(total:number){
    this.total=total;
  }
  
  insertCliente(cliente: any){
     return this.httpClient.post<any>(this.urlCliente+"/insert",cliente)
  }

  putCliente(cliente: any, nit: string){
    return this.httpClient.put<any>(this.urlCliente+"/"+nit,cliente)
 }
 getCliente(nit: string){
  return this.httpClient.get<any>(this.urlCliente+"/"+nit)
 }
}
