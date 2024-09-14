import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';


@Component({
  selector: 'app-cajero',
  standalone: true,
  imports: [RouterLink,RouterLinkActive,RouterOutlet],
  templateUrl: './cajero.component.html',
  styleUrl: './cajero.component.css'
})
export   default  class CajeroComponent {

}
