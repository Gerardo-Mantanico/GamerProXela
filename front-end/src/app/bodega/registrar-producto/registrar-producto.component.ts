import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { ProductosService } from '../../service/bodega/productos.service';
import { AuthServiceService } from '../../service/autoservice/auth-service.service';

@Component({
  selector: 'app-registrar-producto',
  standalone: true,
  imports: [ReactiveFormsModule,CommonModule],
  templateUrl: './registrar-producto.component.html',
  styleUrl: './registrar-producto.component.css'
})
export  default class RegistrarProductoComponent {
  public form: FormGroup;
  public categoria!: string;
  public visibleConsola: boolean = false;
  public visibleVideojuego: boolean = false;
  public producto: any;
  private data : any;

  constructor(private formBuilder: FormBuilder, private service: ProductosService, private authservie: AuthServiceService) {
    this.form = this.formBuilder.group({
      cantidad: ['',[Validators.required]]
    });

   
  }

  onEnter(event: KeyboardEvent): void {
    if (event.key === 'Enter') {
        const inputElement = event.target as HTMLInputElement;
        const inputValue = inputElement.value;
        this.getProduct(inputValue)
    }
  
  }


  onChanges(categoria: string): void {
  
    if(categoria=="Consola"){
      this.visibleConsola = true;
      this.visibleVideojuego=false;
    }
    else{
       this.visibleVideojuego = true
       this.visibleConsola=false;
    }

    
  }

  getProduct(codigo: string){
    this.service.get(codigo).subscribe(
      data =>{
        console.log('Datos obtenidos:', data);
        this.producto=data;
        this.onChanges(data.categoria);
      },
      error => {
        console.error('Error en la solicitud:', error);
      }
    );
  }

  onSubmit(){
    if(this.form.value.cantidad!=null){
      this.data= this.authservie.getCredentials()!
      this.service.insertProduct(
        {
            "id_bodega": this.data.dato_extra            ,
            "id_producto": this.producto.id,
            "cantidad": this.form.value.cantidad
        }
      ).subscribe({
        next: (response) => {
          console.log('Empleado agregado exitosamente:', response);
        },
        error: (err) => {
           
          console.error('Error al agregar empleado:', err);
        }
      })
    }}

  }
        

    
    
    

