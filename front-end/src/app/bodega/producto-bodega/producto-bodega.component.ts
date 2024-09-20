import { Component } from '@angular/core';
import { ProductosService } from '../../service/bodega/productos.service';
import { AuthServiceService } from '../../service/autoservice/auth-service.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-producto-bodega',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './producto-bodega.component.html',
  styleUrl: './producto-bodega.component.css'
})
export default class ProductoBodegaComponent {
  credencial: any
  cosola: any[] = [];
  videojuego: any[]=[];
  productos: any;
  v: any;

  constructor(private Productoservice: ProductosService, private authservice: AuthServiceService){
    this.getProduc();
  }
  getProduc(){
    this.credencial= this.authservice.getCredentials()!;
    this.Productoservice.getListProduct(this.credencial.dato_extra).subscribe({
      next: (response: any) =>{
        this.videojuego=response.videojuego;
        console.log(this.videojuego)
        this.cosola= response.consola
      },
      error: (error) =>{
        console.log(error)
      }
    })
  }

}
