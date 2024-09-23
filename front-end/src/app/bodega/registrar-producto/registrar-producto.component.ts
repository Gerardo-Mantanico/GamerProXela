import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { ProductosService } from '../../service/bodega/productos.service';
import { AuthServiceService } from '../../service/autoservice/auth-service.service';
import Swal from 'sweetalert2'

@Component({
  selector: 'app-registrar-producto',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './registrar-producto.component.html',
  styleUrl: './registrar-producto.component.css'
})
export default class RegistrarProductoComponent {
  public form!: FormGroup;
  public categoria!: string;
  public visibleConsola: boolean = false;
  public visibleVideojuego: boolean = false;
  public producto: any;
  private data: any;
  private inputElement: any;

  constructor(private formBuilder: FormBuilder, private service: ProductosService, private authservie: AuthServiceService) {
    this.form = this.formBuilder.group({
      cantidad: ['', [Validators.required]]
    });
  }

  onEnter(event: KeyboardEvent): void {
    if (event.key === 'Enter') {
      this.inputElement = event.target as HTMLInputElement;
      const inputValue = this.inputElement.value;
      this.getProduct(inputValue)
    }
  }


  onChanges(categoria: string): void {
    if (categoria == "Consola") {
      this.visibleConsola = true;
      this.visibleVideojuego = false;
    }
    else {
      this.visibleVideojuego = true
      this.visibleConsola = false;
    }
  }

  getProduct(codigo: string) {
    this.service.get(codigo).subscribe(
      data => {
       Swal.fire({
            title: 'Cargando...',
            text: 'Por favor espera.',
            allowOutsideClick: false, // Deshabilitar el clic fuera para cerrar
            timer:400,
            didOpen: () => {
              Swal.showLoading(); // Mostrar el loader
            }
          });
          console.log('Datos obtenidos:', data);
          this.producto = data;
          this.onChanges(data.categoria);
      },
      error => {
        Swal.fire({
          position: "top-end",
          icon: "error",
          title: "No existe ningún producto",
          showConfirmButton: false,
          timer: 1500
        });
        console.error('Error en la solicitud:', error);
      }
    );
  }

  //metodo para registrar producto
  onSubmit() {
    if (this.form.value.cantidad != null) {
      this.data = this.authservie.getCredentials()!
      this.service.insertProduct(
        {
          "id_bodega": this.data.dato_extra,
          "id_producto": this.producto.id,
          "cantidad": this.form.value.cantidad
        }
      ).subscribe({
        next: (response) => {
          Swal.fire({
            position: "top-end",
            icon: "success",
            title: "Producto ingresado",
            showConfirmButton: false,
            timer: 1500
          });
          this.clear()

        },
        error: (err) => {
          Swal.fire({
            position: "top-end",
            icon: "error",
            title: "Ocurrio un error  a la hora de ingresar un producto",
            showConfirmButton: false,
            timer: 1500
          });
        }
      })
    }
  }


  clear() {
    this.producto.nombre = ""
    this.producto.cantidad = " "
    this.producto.precio = ""
    this.producto.categoria = ""
    this.producto.descripcion = " "
    this.visibleConsola = false;
    this.visibleVideojuego = false;
    this.inputElement.value = ""
  }
}






