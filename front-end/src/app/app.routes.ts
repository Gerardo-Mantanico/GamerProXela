import { Routes } from '@angular/router';


export const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'login', loadComponent:()=> import('./login/login.component'),
    children:[


        
    ]
   },

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
          },
          {
            path:'sucursal',loadComponent: () => import('./admin/sucursal/sucursal.component'),
          },
          {
            path:'historial',loadComponent: () => import('./admin/historial/historial.component')
          },
          {
            path:'reportesAdmin', loadComponent:() => import('./admin/reportes/reportes.component')
          }
      ]
  },
  {
    path: 'bodega', loadComponent: () =>import ('./bodega/bodega.component'),
    children:[
        {
          path: "ingresarProductos", loadComponent:() => import('./bodega/registrar-producto/registrar-producto.component')
        },
        {
          path: "producto", loadComponent : () =>import('./bodega/producto-bodega/producto-bodega.component')
        }
    ]
  }
];
