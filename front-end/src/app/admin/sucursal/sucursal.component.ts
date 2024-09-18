import { Component } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, FormGroup, Validators } from '@angular/forms';
import { Sucursal } from '../../model/sucursal';
import { ServicioSucursalService } from '../../service/sucursal/servicio-sucursal.service';




@Component({
  selector: 'app-sucursal',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './sucursal.component.html',
  styleUrl: './sucursal.component.css'
})
export default class SucursalComponent {
  public checkoutForm;

  constructor(private serviceS: ServicioSucursalService, private formBuilder: FormBuilder) {
    this.checkoutForm = this.formBuilder.group({
      codeBranch: ['', [Validators.required]],
      name: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      address: ['', [Validators.required]],
      phone: ['', [Validators.required]],
      timeOpen: ['', [Validators.required]],
      timeClosed: ['', [Validators.required]]
    });
  }

  ngOnInit() {

    //this.items = this.cartService.getItems();
  }


  onSubmit() {
    console.warn('Your order has been submitted', this.checkoutForm.value.timeOpen);
    const sucursal = new Sucursal(
      1,
      this.checkoutForm.value.address!,
      this.checkoutForm.value.name!,
      1,
      this.checkoutForm.value.codeBranch!,
      this.checkoutForm.value.email!,
      parseInt(this.checkoutForm.value.phone!, 10),
      this.checkoutForm.value.timeOpen!+":00",
      this.checkoutForm.value.timeClosed!+":00"
    );
    
     console.log(sucursal)
    this.add(sucursal)
   // this.checkoutForm.reset();
  }

  add(sucural: Sucursal): void {
    this.serviceS.insert(sucural).subscribe(
      {
        error: (err) => {
          console.error('Login failed:', err);
        }
      }
    )
  }

  
} 
