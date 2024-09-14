import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';

export const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },

  {
    path: 'cajero', loadComponent: () => import('./cajero/cajero.component'),
      children: [
        {
          path: 'descuento', loadComponent: () => import('./cajero/tarjeta-descuento/tarjeta-descuento.component')
        },
        {
          path: 'venta', loadComponent: () => import('./cajero/venta/venta.component')
        },
        {
          path: 'factura', loadComponent:()=>import('./cajero/factura/factura.component')
        }

      ]
  },
  {
    path: 'admin', loadComponent: () => import('./admin/admin.component'),
      children: [ 
          {
            path:'registrar-empleado', loadComponent: ()=> import('./admin/registrar-empleado/registrar-empleado.component'),
          }
          
      ]
  },
];
