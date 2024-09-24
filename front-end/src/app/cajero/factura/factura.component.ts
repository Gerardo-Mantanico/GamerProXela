import { Component } from '@angular/core';
import { FacturaService } from '../../service/caja/factura.service';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { AuthServiceService } from '../../service/autoservice/auth-service.service';
import { Factura } from '../../model/factura';
import Swal from 'sweetalert2';
import {  Router } from '@angular/router';

@Component({
  selector: 'app-factura',
  standalone: true,
  imports: [CommonModule,ReactiveFormsModule],
  templateUrl: './factura.component.html',
  styleUrl: './factura.component.css'
})
export default class FacturaComponent {
  credencial: any;
  public listProductos: any;
  public total: number;
  public facturaForm: FormGroup;
  private inputElement: any;
  public cliente! : any;
  public CliEstao=false;
  public facEstado=false;
  private idCliente!: number;

  constructor(
    private facturaservice: FacturaService,
    private formBuilder: FormBuilder,
    private authservice: AuthServiceService,
    private  router: Router
   
  ) {
    this.listProductos = this.facturaservice.getListaProductos();
    console.log("productos "+this.listProductos)
    this.total = this.facturaservice.getTotal();
    this.credencial = this.authservice.getCredentials()!;

    this.facturaForm = this.formBuilder.group({
      nit: ['', [Validators.required]],
      nombre: ['', [Validators.required]],
      email: ['', [Validators.required]],
      direccion: ['', [Validators.required]],
      telefono: ['', [Validators.required]],
      codigoTarjeta: ['', [Validators.required]],
    });

  
  }

  onSubmit() {
    if (this.facturaForm.valid) {
      console.log(this.facturaForm.value);
      // Lógica adicional para manejar la sumisión del formulario
    }
  }
  onSearchNit(event: KeyboardEvent): void {
    if (event.key === 'Enter') {
      this.inputElement = event.target as HTMLInputElement;
      const nit = this.inputElement.value;
      console.log("hola" + nit)
      this.searchNit(nit);
      this.CliEstao=false;
      this.facEstado=false;
    }
  }

  searchNit(nit:string){
    this.facturaservice.getCliente(nit).subscribe({
      next: (response)=>{
         if(response==null){
          this.CliEstao=true
         }
         this.idCliente= response.id_cliente
         this.facturaForm.patchValue({nombre: response.nombre});
         this.facturaForm.patchValue({direccion: response.direccion});
         this.facturaForm.patchValue({telefono: response.telefono});
         console.log(response.id_cliente)
         this.facEstado=true;
          
        
      },
      error: (err) =>{
        this.CliEstao=true;
      }
    })
  }

  registerCliente(){

    this.facturaservice.insertCliente({
      "id_cliente": 0,
      "nombre": this.facturaForm.value.nombre,
      "nit": this.facturaForm.value.nit,
      "telefono": this.facturaForm.value.telefono,
      "direccion": this.facturaForm.value.direccion
     }).subscribe({
      next: (response)=>{
        this.idCliente= response.id_cliente;
        Swal.fire({
          position: "top-end",
          icon: "success",
          title: "Cliente registrado",
          showConfirmButton: false,
          timer: 2000
        });
         this.CliEstao=false;
         this.facEstado=true;
      },
      error :(err)=>{
        Swal.fire({
          position: "top-end",
          icon: "error",
          title: "Error no se pudo registrar al cliente ",
          showConfirmButton: false,
          timer: 2000
        });
      }
      
     })
  }

  generarFactura(){
    const  factura = new Factura(
      this.idCliente,
      this.credencial.id_sucursal,
      this.credencial.id_empleado,
       this.total.toString(),
      "0",
      this.listProductos
    );
  
    console.log(factura)
    this.facturaservice.insertFactura(factura).subscribe({
      next: (response)=>{
        console.log(response);
        Swal.fire({
          position: "top-end",
          icon: "success",
          title: "Factura Generada con exito",
          showConfirmButton: false,
          timer: 2000
        });  
        this.router.navigate(['cajero/venta']);
      },
      error: (err)=>{
        Swal.fire({
          position: "top-end",
          icon: "error",
          title: "Ocurrió un error al intentar realizar la factura. Por favor, verifica que todos los campos sean correctos y vuelve a intentarlo.  ",
          showConfirmButton: false,
          timer: 2000
        });
      }
    })
  }
}



