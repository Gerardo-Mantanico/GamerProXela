import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ReporteService } from '../../service/admin/reporte/reporte.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-historial',
  standalone: true,
  imports: [FormsModule,CommonModule],
  templateUrl: './historial.component.html',
  styleUrl: './historial.component.css'
})
export default class HistorialComponent {
  fechaInicial: string = '';
  fechaFinal: string = '';
  public historial : any[]=[];
  constructor(private reportes: ReporteService) {}

  onSubmit() {
    this.reportes.historial({
      inicio: this.fechaInicial,
      final: this.fechaFinal
    }).subscribe({
      next: (response)=>{
        this.historial=response;
      },
      error:(err)=>(
        console.log("Ocurrio un error")
      )
    })

   }
}
