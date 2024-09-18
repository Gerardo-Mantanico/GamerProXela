import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {

  constructor() { }


  // Método para guardar credenciales en localStorage
  saveCredentials(token: string): void {
    localStorage.setItem('authToken', token);
  }

  // Método para obtener credenciales desde localStorage
  getCredentials(): string | null {
    return  JSON.parse(localStorage.getItem('authToken')!);
  }

  // Método para eliminar credenciales de localStorage
  removeCredentials(): void {
    localStorage.removeItem('authToken');
  }
}
