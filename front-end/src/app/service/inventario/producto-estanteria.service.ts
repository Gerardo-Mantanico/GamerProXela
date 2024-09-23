import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductoEstanteriaService {


  private PRODUCT_URL = 'http://0.0.0.0:8080/produc-rack/'

  constructor( private httpClient: HttpClient){ }

  insertProduct(product: any){
    console.log(product)
     return this.httpClient.post<any>(this.PRODUCT_URL+"insert", product)
  }
  getListProduct(id : number){
      return this.httpClient.get<any>(this.PRODUCT_URL+id)
  }
  getProductEstanteria(id: number){
     return this.httpClient.get<any>(this.PRODUCT_URL+"list/"+id)
  }
  getpasillos(id:number){
    return this.httpClient.get<any>("http://0.0.0.0:8080/estanteria/pasillo/"+id)
  }
  searchProduct(producto : any):Observable<any>{
    console.log(producto)
    return this.httpClient.post<any>(this.PRODUCT_URL+"producto-estanteria",producto)
  }
}
