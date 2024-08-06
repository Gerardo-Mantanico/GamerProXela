import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterOutlet,RouterLink } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { CajeroComponent } from './cajero/cajero.component';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet,RouterLink, CajeroComponent , LoginComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'GamerProXela';
}
