import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Route, Router } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
 
  private LOGIN_URL = 'http://0.0.0.0:8080/login/insert'
  
  constructor( private httpClient: HttpClient, private router: Router){ }

  login(credencial: any):Observable<any>{
    return this.httpClient.post<any>(this.LOGIN_URL,credencial)
  }
}
