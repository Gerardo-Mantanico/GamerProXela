import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { Sucursal } from '../../model/sucursal';



@Injectable({
  providedIn: 'root'
})

export class ServicioSucursalService {
  private LOGIN_URL = 'http://0.0.0.0:8080/branch/'
  constructor(private httpClient: HttpClient, private router: Router) { }



  /** POST: add a new branch to the server */
  insert(sucural: Sucursal): Observable<Sucursal> {
    return this.httpClient.post<Sucursal>(this.LOGIN_URL + "insert", sucural)
  }

}
