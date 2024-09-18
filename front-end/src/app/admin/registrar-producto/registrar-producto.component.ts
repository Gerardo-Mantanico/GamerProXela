import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-registrar-producto',
  standalone: true,
  imports: [ReactiveFormsModule,CommonModule],
  templateUrl: './registrar-producto.component.html',
  styleUrl: './registrar-producto.component.css'
})
export  default class RegistrarProductoComponent {
  public form: FormGroup;
  public categorias: string[] = ['Consola', 'Videojuego'];
  public visibleConsola: boolean = false;
  public visibleVideojuego: boolean = false;

  constructor(private fb: FormBuilder) {
    this.form = this.fb.group({
      categoria: ['', Validators.required],
    });

    this.onChanges();
  }

  onChanges(): void {
    this.form.get('categoria')?.valueChanges.subscribe(value => {
      this.visibleConsola = value === 'Consola'; 
      this.visibleVideojuego = value ==='Videojuego'
    });
  }
}
