import { Component } from '@angular/core';
import { Router, RouterLink, RouterOutlet } from '@angular/router';
import { AuthServiceService } from '../service/autoservice/auth-service.service';
@Component({
  selector: 'app-admin',
  standalone: true,
  imports: [RouterOutlet,RouterLink],
  templateUrl: './admin.component.html',
  styleUrl: './admin.component.css'

})
export default class AdminComponent {
  nameBranch 
  data: any

  constructor(private authService: AuthServiceService, private router: Router){
    this.data= this.authService.getCredentials()!;
    this.nameBranch= this.data.nombre;   
  }

  closed(){
    this.authService.removeCredentials();
    this.router.navigate(['login']);
  }

}
