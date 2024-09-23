import { Component } from '@angular/core';
import Swal from 'sweetalert2';
import { ProductosService } from '../../service/bodega/productos.service';
import { AuthServiceService } from '../../service/autoservice/auth-service.service';
import { ProductoEstanteriaService } from '../../service/inventario/producto-estanteria.service';
import { CommonModule } from '@angular/common';
import { Producto } from '../../model/producto';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-venta',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './venta.component.html',
  styleUrl: './venta.component.css'
})

export default class VentaComponent {
credencial: any
private inputElement: any;
public producto: Producto;
public productos! :Producto[]

constructor( private authservice: AuthServiceService, private productoestanteria: ProductoEstanteriaService) {
  this.credencial = this.authservice.getCredentials()!
  this.producto = new Producto();
}


onSearchCode(event: KeyboardEvent): void {
  if (event.key === 'Enter') {
    this.inputElement = event.target as HTMLInputElement;
    const codigoProdcuto = this.inputElement.value;
    this.getSearchProduct(codigoProdcuto, " ")
  }
}

onSearchName(event: KeyboardEvent): void {
  if (event.key === 'Enter') {
    this.inputElement = event.target as HTMLInputElement;
    const NameProdcuto = this.inputElement.value;
    this.getSearchProduct("",NameProdcuto)
  }
}


getSearchProduct(codigo: string, nombre: string) {
  this.productoestanteria.searchProduct({
      "id_sucursal": this.credencial.id_sucursal,
      "codigo_producto": codigo,
      "nombre": nombre
  }).subscribe({
      next: (response: Producto) => {
          console.log('Respuesta de la API:',  response);
          this.producto=response;
        
          
      },
      error: (err) => {
          console.error('Error al buscar producto:', err);
      }
  });
}

agregar(){
 console.log( this.producto.existencia)

}

actualizarCantidad(nuevaCantidad:number) {
  // Suponiendo que 'producto' es un objeto global, o lo puedes obtener de donde lo necesites
  this.producto.existencia = nuevaCantidad;
  // Si necesitas actualizar la vista, puedes hacerlo aquí también
 // console.log(producto); // Muestra el objeto actualizado en la consola
}

}
