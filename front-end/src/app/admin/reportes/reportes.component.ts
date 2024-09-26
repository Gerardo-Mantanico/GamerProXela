import { Component } from '@angular/core';
import { ReporteService } from '../../service/admin/reporte/reporte.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-reportes',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './reportes.component.html',
  styleUrl: './reportes.component.css'
})
export default class ReportesComponent {
  public Clientes: any[] = [];
  public Productos: any[] = [];
  public Sucursal: any[] = [];
  public Ventas: any[] = [];
  fechaInicial: string = '';
  fechaFinal: string = '';

  constructor(private reporteService: ReporteService){
    this.clienteGastador();
    this.articulo();
    this.sucursal();
   
  }

  clienteGastador(){
    this.reporteService.ClienteGastador().subscribe({
      next: (respoonse)=>{
        this.Clientes= respoonse;
      },
      error:(err)=>{

      }
    })
  }

  articulo(){
    this.reporteService.topArticulos().subscribe({
      next: (respoonse)=>{
        this.Productos= respoonse;
      },
      error:(err)=>{

      }
    })
  }

  sucursal(){
    this.reporteService.topSucursal().subscribe({
      next: (respoonse)=>{
        this.Sucursal= respoonse;
      },
      error:(err)=>{

      }
    })
  }

  venta(data: any){
    this.reporteService.ventasGrandes(data).subscribe({
      next: (respoonse)=>{
        this.Ventas= respoonse;
      },
      error:(err)=>{

      }
    })
  }
  onSubmit(){
    const data = {
      inicio: this.fechaInicial,
      final: this.fechaFinal
    };
    console.log(data)
    this.venta(data);
  }
}
