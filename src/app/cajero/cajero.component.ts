import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { VentaComponent } from "./venta/venta.component";
import { FacturaComponent } from "./factura/factura.component";

@Component({
  selector: 'app-cajero',
  standalone: true,
  imports: [RouterOutlet,RouterLink],
  templateUrl: './cajero.component.html',
  styleUrl: './cajero.component.css'
})
export class CajeroComponent {

}
