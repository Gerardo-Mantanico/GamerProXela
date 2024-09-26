import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { FacturaService } from '../../service/caja/factura.service';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-tarjeta-descuento',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './tarjeta-descuento.component.html',
  styleUrl: './tarjeta-descuento.component.css'
})
export default class TarjetaDescuentoComponent {

  public statusmsj=false;
  public statuserr=false;
  public forms: FormGroup

  constructor(private facturaservice: FacturaService, private formBuilder: FormBuilder){
    this.forms =  this.formBuilder.group({
      nit: ['', [Validators.required]],
    })
    
  }

  
  onSubmit(){
    console.log("hola")
    this.facturaservice.generateCard(this.forms.value.nit).subscribe({
      next: (response)=>{
        this.statusmsj=true;
        this.statuserr=false;
        this.forms.reset()
      },
      error: (err)=>{
        this.statuserr=true;
        this.statusmsj=false;
      }
      
    })
  }

}
