import { Component } from '@angular/core';
import { LoginService } from '../service/login.service';
import { FormBuilder, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router, RouterLink, RouterOutlet } from '@angular/router';
import { Credencial } from '../inteface/credencial';
import { AuthServiceService } from '../service/autoservice/auth-service.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export default class LoginComponent {

  checkoutForm

  constructor(private service: LoginService, private formBuilder: FormBuilder, private router: Router, private authService: AuthServiceService) {
    this.checkoutForm = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
    })
  }


  onSubmit() {
      this.service.login(this.checkoutForm.value).subscribe({
        next: (response: Credencial) => {
          this.authService.saveCredentials(JSON.stringify(response));
          
          if(response.rol=='A'){
             this.router.navigate(['admin/reportesAdmin']);
          }
          else if(response.rol=='B'){
            this.router.navigate(['bodega/ingresarProductos']);
          }
          else if(response.rol=='C'){
            this.router.navigate(["cajero/venta"]);
          }
          else if (response.rol=='I'){
            this.router.navigate(['inventario/trasladarProducto']);
          }

        },
        error: (err) => {
          this.checkoutForm.reset
          Swal.fire({
            position: "top-end",
            icon: "error",
            title: "credenciales incorrectas",
            showConfirmButton: false,
            timer: 2000
          });
          
        }
      });
    }
  }



