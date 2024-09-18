import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Empleado } from '../../../model/empleado';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RegistroEmpleadoSService {
  private LOGIN_URL = 'http://0.0.0.0:8080/user/'

  constructor(private httpClient: HttpClient, private router: Router) { }
  /** POST: add a new branch to the server */
  insert(empleado: Empleado): Observable<Empleado> {
    return this.httpClient.post<Empleado>(this.LOGIN_URL + "cashier", empleado)
  }
 
  get(id: string): Observable<any>{
    return this.httpClient.get<any>(this.LOGIN_URL+"users/"+id)
  }
}
