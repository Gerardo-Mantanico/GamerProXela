import { Component, NgModule } from '@angular/core';
import { RouterModule,Routes } from '@angular/router';
import { CajeroComponent } from './cajero/cajero.component';
import { LoginComponent } from './login/login.component';
import { VentaComponent } from './cajero/venta/venta.component';
import { FacturaComponent } from './cajero/factura/factura.component';

export const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  {path:'login',component:LoginComponent},
  {path:'cajero',component:CajeroComponent},
  {path:'venta',component:VentaComponent},
  {path:'factura',component:FacturaComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
