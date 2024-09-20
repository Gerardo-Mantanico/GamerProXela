import { Component, NgModule } from '@angular/core';
import { ProductoEstanteriaService } from '../../service/inventario/producto-estanteria.service';
import { AuthServiceService } from '../../service/autoservice/auth-service.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-productos-estanteria',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './productos-estanteria.component.html',
  styleUrl: './productos-estanteria.component.css'
})
export default class ProductosEstanteriaComponent {
  public productos: any[] = [];
  credencial: any
  constructor(private service: ProductoEstanteriaService, private auth: AuthServiceService) {
    this.getProductos();
  }


  getProductos() {
    this.credencial = this.auth.getCredentials();
    this.service.getProductEstanteria(this.credencial.dato_extra).subscribe({
      next: (response) => {
        this.productos = response.productos;
        console.log(this.productos)
      }
    })
  }

}
