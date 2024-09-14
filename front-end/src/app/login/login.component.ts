import { Component } from '@angular/core';
import { LoginService } from '../service/login.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { Credencial } from '../inteface/credencial';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule,CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  user: string ='luis@gmail.com';
  password:  string="123456";


  constructor(private service: LoginService, private router: Router){}

  login(): void {
    this.service.login(this.user, this.password).subscribe({
      next: (response: Credencial) => {
        console.log('Login successful:', response);

        // Accede a los atributos de la respuesta
        const idEmpleado = response.id_empleado;
        const idSucursal = response.id_sucursal;
        const rol = response.rol;
        const dataExtra = response['data exta']; // Accede al atributo con nombre especial

        console.log('ID Empleado:', idEmpleado);
        console.log('ID Sucursal:', idSucursal);
        console.log('Rol:', rol);
        console.log('Data Extra:', dataExtra);

        // Aquí puedes manejar los datos, por ejemplo guardarlos en un servicio de autenticación

        this.router.navigate(['/cajero']);
      },
      error: (err) => {
        console.error('Login failed:', err);
      }
    });
  }
}