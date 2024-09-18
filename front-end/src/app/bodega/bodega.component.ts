import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { AuthServiceService } from '../service/autoservice/auth-service.service';

@Component({
  selector: 'app-bodega',
  standalone: true,
  imports: [RouterOutlet, RouterLink],
  templateUrl: './bodega.component.html',
  styleUrl: './bodega.component.css'
})
export  default class BodegaComponent {
  public branch
  private data: any;
  constructor(private authservice: AuthServiceService){
    this.data= this.authservice.getCredentials()!;
    this.branch= this.data.nombre;   
  }

}
