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
  pasillos!: any[];
  public detailProducto: any;
  public estadoVideojugo = false;
  public estadoConsola = false;


  constructor(private Productoservice: ProductosService, private authservice: AuthServiceService, private productoestanteria: ProductoEstanteriaService) {
    this.getProduc();
    this.getNoPasillos();
  }
  
  getProduc() {
    this.credencial = this.authservice.getCredentials()!;
    console.log(this.credencial.id_sucursal)
    this.Productoservice.getListProductEstanteria(this.credencial.id_sucursal).subscribe({
      next: (response: any) => {
        this.videojuego = response.videojuego;
        this.consola = response.consola
        this.details(0, 2)
      },
      error: (error) => {
        console.log(error)
      }
    })
  }

  details(indice: number, tipo: number) {
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
    let opcionesHTML = '';
    for (const pasillo of this.pasillos) {
      opcionesHTML += `<option value="${pasillo.id_pasillo}">Pasillo ${pasillo.no}: ${pasillo.descripcion}</option>`;
    }

    const { value: result } = await Swal.fire({
      title: 'Ingresar producto a estantería',
      html: `
        <input id="swal-input1" class="swal2-input" placeholder="Cantidad" type="number" required  min="1">
        <select id="select" class="swal2-input">
          ${opcionesHTML}
        </select>
      `,
      focusConfirm: false,
      preConfirm: () => {
        const input1 = (<HTMLInputElement>document.getElementById('swal-input1')).value;
        const input2 = (<HTMLInputElement>document.getElementById('select')).value;
        return { cantidad: input1, no_pasillo: input2 };
      },
      showCancelButton: true,
    });
  
    if (result) {
      const cantidadIngresada = parseInt(result.cantidad);
      const no_pasillo = parseInt(result.no_pasillo);
      if (  cantidadIngresada>0 && cantidadIngresada<=cantidadMax  && no_pasillo!=null ) {

         if(tipo==1){
          this.inserEstanteria(this.consola[indice].id, no_pasillo,cantidadIngresada)
            console.log(this.consola[indice].cantidad-cantidadIngresada)
            this.consola[indice].cantidad = this.consola[indice].cantidad-cantidadIngresada;

         }
         else{
          this.inserEstanteria(this.videojuego[indice].id ,no_pasillo,cantidadIngresada)
          this.videojuego[indice].cantidad =  this.videojuego[indice].cantidad-cantidadIngresada;
          console.log(this.videojuego[indice].cantidad)
         }
        Swal.fire(`Cantidad ingresada: ${result.cantidad}, Producto: ${result.producto}`);
      }
       else {

        Swal.fire('Las unidades maximas que puede ingresar son ' + cantidadMax+"");
        }
    }
  }  


  inserEstanteria(id: number, no_pasillo: number,cantidad: number){
    this.productoestanteria.insertProduct(
        {
          "id_estanteria": this.credencial.dato_extra,
          "id_producto": id,
          "id_pasillo": no_pasillo,
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

  getNoPasillos(){
    this.productoestanteria.getpasillos(this.credencial.id_sucursal).subscribe({
      next: (response)=>{
        this.pasillos=response.pasillo;
      },
      error: (error)=>{

      }
    })
  }

}
