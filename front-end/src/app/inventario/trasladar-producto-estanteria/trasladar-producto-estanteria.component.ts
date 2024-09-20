import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { AuthServiceService } from '../../service/autoservice/auth-service.service';
import { ProductosService } from '../../service/bodega/productos.service';
import { CommonModule } from '@angular/common';
import Swal from 'sweetalert2'
import { ProductoEstanteriaService } from '../../service/inventario/producto-estanteria.service';

@Component({
  selector: 'app-trasladar-producto-estanteria',
  standalone: true,
  imports: [RouterOutlet, CommonModule],
  templateUrl: './trasladar-producto-estanteria.component.html',
  styleUrl: './trasladar-producto-estanteria.component.css'
})
export default class TrasladarProductoEstanteriaComponent {

  credencial: any
  consola: any[] = [];
  videojuego: any[] = [];
  productos: any;
  public detailProducto: any;
  public estadoVideojugo = false;
  public estadoConsola = false;


  constructor(private Productoservice: ProductosService, private authservice: AuthServiceService, private productoestanteria: ProductoEstanteriaService) {
    this.getProduc();
   
  }
  
  getProduc() {
    this.credencial = this.authservice.getCredentials()!;
    this.Productoservice.getListProduct(19).subscribe({
      next: (response: any) => {
        this.videojuego = response.videojuego;
        console.log(this.videojuego)
        this.consola = response.consola
        this.details(0, 2)
      },
      error: (error) => {
        console.log(error)
      }
    })
  }

  details(indice: number, tipo: number) {
    console.log(indice + "   " + tipo)
    if(tipo==1){
      this.detailProducto = this.consola[indice]
      this.estadoConsola=true;
      this.estadoVideojugo=false;
    }
    else{
      this.detailProducto = this.videojuego[indice]
      this.estadoConsola=false;
      this.estadoVideojugo=true;
    }
  }


  async insertInvet(indice: number, tipo: number, cantidadMax: number) {
    const { value: result } = await Swal.fire({
      title: 'Ingresar producto a estantería',
      html: `
        <input id="swal-input1" class="swal2-input" placeholder="Cantidad" type="number" required  min="1">
        <input id="swal-input2" class="swal2-input" placeholder="No. de pasillo" type="text" required>
      `,
      focusConfirm: false,
      preConfirm: () => {
        const input1 = (<HTMLInputElement>document.getElementById('swal-input1')).value;
        const input2 = (<HTMLInputElement>document.getElementById('swal-input2')).value;
        return { cantidad: input1, no_pasillo: input2 };
      },
      showCancelButton: true,
    });
  
    if (result) {
      const cantidadIngresada = parseInt(result.cantidad);
      if (  cantidadIngresada>0 && cantidadIngresada<=cantidadMax  && result.no_pasillo!=null ) {

         if(tipo==1){
          this.inserEstanteria(this.consola[indice].id_producto_bodega ,result.no_pasillo,cantidadIngresada)
         }
         else{
          this.inserEstanteria(this.videojuego[indice].id_producto_bodega ,result.no_pasillo,cantidadIngresada)
         }
        Swal.fire(`Cantidad ingresada: ${result.cantidad}, Producto: ${result.producto}`);
      }
       else {

        Swal.fire('Las unidades maximas que puede ingresar son ' + cantidadMax+"");
        }
    }
  }  


  inserEstanteria(id: number, no_pasillo: string,cantidad: number){
    this.productoestanteria.insertProduct(
        {
          "id_estanteria": this.credencial.dato_extra,
          "id_producto_bodega": id,
          "no_pasillo": no_pasillo,
          "cantidad": cantidad
        }
    ).subscribe({
      next: (reponse)=>{
        const Toast = Swal.mixin({
          toast: true,
          position: "top-end",
          showConfirmButton: false,
          timer: 3000,
          timerProgressBar: true,
          didOpen: (toast) => {
            toast.onmouseenter = Swal.stopTimer;
            toast.onmouseleave = Swal.resumeTimer;
          }
        });
        Toast.fire({
          icon: "success",
          title: "Producto insertado en estanteria"
        });
      },
      error: (err)=>{
      }
    })
  }

}
