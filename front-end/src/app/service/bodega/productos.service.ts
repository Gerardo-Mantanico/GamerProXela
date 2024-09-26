import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductosService {

  private LOGIN_URL = 'http://0.0.0.0:8080/product/'
  private PRODUCT_URL = 'http://0.0.0.0:8080/product-bodega/'

  constructor( private httpClient: HttpClient){ }

  get(id: string): Observable<any>{
    return this.httpClient.get<any>(this.LOGIN_URL+id)
  }

  insertProduct(product: any){
     return this.httpClient.post<any>(this.PRODUCT_URL+"insert", product)
  }
  getListProduct(id : number){
      return this.httpClient.get<any>(this.PRODUCT_URL+id)
  }

  getListProductEstanteria(id : number){
    return this.httpClient.get<any>(this.PRODUCT_URL+"estanteria/"+id)
}
}
