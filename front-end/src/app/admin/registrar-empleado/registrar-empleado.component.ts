import { Component } from '@angular/core';
import { RegistroEmpleadoSService } from '../../service/admin/registrarEmpleado/registro-empleado-s.service';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { Empleado } from '../../model/empleado';
import { AuthServiceService } from '../../service/autoservice/auth-service.service';
import { User } from '../../model/user';
import { CommonModule } from '@angular/common'; 
import Swal from 'sweetalert2';

@Component({
  selector: 'app-registrar-empleado',
  standalone: true,
  imports: [ReactiveFormsModule,CommonModule],
  templateUrl: './registrar-empleado.component.html',
  styleUrl: './registrar-empleado.component.css'
})
export default class RegistrarEmpleadoComponent {
    checkoutForm;
    public branch;
    private Credential: any;
    userData: User[] = [];
  constructor(private service: RegistroEmpleadoSService,private formBuilder: FormBuilder, private authServide: AuthServiceService) {
      this.checkoutForm = this.formBuilder.group({
      name: ['', [Validators.required]],
      user: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      address: ['', [Validators.required]],
      phone: ['', [Validators.required]],
      rol: ['', [Validators.required]],
      password: ['', Validators.required],
    })
    this.Credential= this.authServide.getCredentials()!;
    this.branch=this.Credential.nombre
    }



  onSubmit() {
    const empleado = new Empleado(
      0,
      this.checkoutForm.value.rol!,
      this.checkoutForm.value.user!,
      this.checkoutForm.value.password!,
      this.Credential.id_sucursal,
      this.checkoutForm.value.name!,
      parseInt(this.checkoutForm.value.phone!),
      this.checkoutForm.value.email!
    );

    console.log(empleado)
    this.add(empleado)
  }

  add(empleado: Empleado): void {
    this.service.insert(empleado).subscribe({
      next: (response) => {
        console.log('Empleado agregado exitosamente:', response);
        const user = new User();
         user.id_empleado = empleado.getId();
         user.nombre = empleado.getNombre();
         user.rol = empleado.getRol();
        this.userData.push(user);
        this.checkoutForm.reset();
        Swal.fire({
          position: "top-end",
          icon: "success",
          title: "Empleado registrado",
          showConfirmButton: false,
          timer: 1500
        });
      },
      error: (err) => {
        Swal.fire({
          position: "top-end",
          icon: "error",
          title: "Ya existe un empleado con esos registros",
          showConfirmButton: false,
          timer: 2000
        });
        console.error('Error al agregar empleado:', err);
      }
    });
  }

  ngOnInit(): void {
    this.fetchUser(this.Credential.id_sucursal); // Llama al servicio con un ID de ejemplo
  }

  fetchUser(id: string): void {
    this.service.get(id).subscribe(
      data => {
        this.userData = data;
        console.log('Datos obtenidos:', this.userData);
      },
      error => {
        console.error('Error en la solicitud:', error);
      }
    );
  }

}
