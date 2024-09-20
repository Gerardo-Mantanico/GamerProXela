import { Component } from '@angular/core';
import {Router, RouterLink, RouterOutlet } from '@angular/router';
import { AuthServiceService } from '../service/autoservice/auth-service.service';

@Component({
  selector: 'app-inventario',
  standalone: true,
  imports: [RouterOutlet, RouterLink],
  templateUrl: './inventario.component.html',
  styleUrl: './inventario.component.css'
})
export default  class InventarioComponent {
  
constructor(private  service: AuthServiceService, private router: Router){}

  closeSession(){
    this.service.removeCredentials();
    this.router.navigate(['login']);
  }


}
