import { Component } from '@angular/core';
import { FacturaService } from '../../service/caja/factura.service';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { AuthServiceService } from '../../service/autoservice/auth-service.service';
import { Factura } from '../../model/factura';

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
  public total: any;
  public facturaForm: FormGroup;
  private inputElement: any;
  public cliente! : any;

  constructor(
    private facturaservice: FacturaService,
    private formBuilder: FormBuilder,
    private authservice: AuthServiceService
  ) {
    this.listProductos = this.facturaservice.getListaProductos();
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
    }
  }

  searchNit(nit:string){
    this.facturaservice.getCliente(nit).subscribe({
      next: (response)=>{
         if(response==null){
         }

         this.facturaForm.patchValue({nombre: response.nombre});
         this.facturaForm.patchValue({direccion: response.direccion});
         this.facturaForm.patchValue({telefono: response.telefono});
         console.log(response.id_cliente)
          
        
      },
      error: (err) =>{
        console.log("no existe")
        this.facturaForm.reset()
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
     }).subscribe();
  }

  generarFactura(cliente: any){
    const  factura = new Factura(
      cliente.id_cliente,
      cliente.nit,
      cliente.nombre,
      cliente.direccion,
      cliente.telefono,
      this.credencial.id_sucursal,
      this.credencial.id_empleado,
      this.total,
      0,
      this.listProductos
    );

  }
}



