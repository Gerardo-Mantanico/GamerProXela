import { Component, DoCheck } from '@angular/core';
import Swal from 'sweetalert2';
import { ProductosService } from '../../service/bodega/productos.service';
import { AuthServiceService } from '../../service/autoservice/auth-service.service';
import { ProductoEstanteriaService } from '../../service/inventario/producto-estanteria.service';
import { CommonModule } from '@angular/common';
import { Producto } from '../../model/producto';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { ProductoFactura } from '../../model/productoFactura';
import { FacturaService } from '../../service/caja/factura.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-venta',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './venta.component.html',
  styleUrl: './venta.component.css'
})

export default class VentaComponent {
  credencial: any
  private inputElement: any;
  public producto!: Producto;
  public productosForm: FormGroup;
  stockProducto!: number
  public hayStock = true;
  listProductos: ProductoFactura[] = [];
  public Total;
  editar = true;

  constructor(private authservice: AuthServiceService, 
    private productoestanteria: ProductoEstanteriaService,
    private formBuilder: FormBuilder,
    private facturaService: FacturaService,
    private router: Router
  ) 
    
    {
    this.credencial = this.authservice.getCredentials()!
    this.producto = new Producto();
    this.productosForm = this.formBuilder.group({
      codigo: ['', [Validators.required]],
      cantidadProducto: ['', [Validators.required]],
      nombre: ['', [Validators.required]],
      precio: [1, [Validators.required]],
      descripcion: [' ', [Validators.required]]
    });
    this.Total = 0;
  }


  onSearchCode(event: KeyboardEvent): void {
    if (event.key === 'Enter') {
      this.inputElement = event.target as HTMLInputElement;
      const codigoProdcuto = this.inputElement.value;
      this.getSearchProduct(codigoProdcuto, " ")
    }
  }

  onSearchName(event: KeyboardEvent): void {
    if (event.key === 'Enter') {
      this.inputElement = event.target as HTMLInputElement;
      const NameProdcuto = this.inputElement.value;
      this.getSearchProduct("", NameProdcuto)
    }
  }


  getSearchProduct(codigo: string, nombre: string) {
    this.productoestanteria.searchProduct({
      "id_sucursal": this.credencial.id_sucursal,
      "codigo_producto": codigo,
      "nombre": nombre
    }).subscribe({
      next: (response: Producto) => {
        console.log('Respuesta de la API:', response);

        this.producto.setcategoria(response.categoria)
        this.producto.setcodigo(response.codigo)
        this.producto.setdescripcion(response.descripcion)
        this.producto.setdescripcionPasillo(response.descripcion_pasillo)
        this.producto.setexistencia(response.existencia)
        this.producto.setidProducto(response.id_producto)
        this.producto.setidProductoEstanteria(response.id_productoEstanteria)
        this.producto.setnoPasillo(response.no_pasillo)
        this.producto.setnombre(response.nombre)
        this.producto.setprecio(response.precio)

        this.stockProducto = this.producto.existencia

      },
      error: (err) => {
        Swal.fire({
          position: "top-end",
          icon: "error",
          title: "No existe ningún producto con ese codigo",
          showConfirmButton: false,
          timer: 2000
        });
        this.productosForm.reset()
      }
    });
  }

  addProduct() {
    const nuevoProducto = new ProductoFactura();

    nuevoProducto.setCodigo(this.producto.codigo)
    nuevoProducto.setNombre(this.producto.nombre)
    nuevoProducto.setCantidad(this.productosForm.value.cantidadProducto)
    nuevoProducto.setPrecio(this.producto.precio)
    nuevoProducto.setSubtotalDescuento(0)
    const cleanedString = nuevoProducto.getPrecio().replace("Q", "").trim();
    const numberValue = parseFloat(cleanedString);
    const subtotal = (numberValue * nuevoProducto.getCantidad()).toFixed(2)
    nuevoProducto.setSubtotal(parseFloat(subtotal));
    this.Total = parseFloat((this.Total + nuevoProducto.getSubtotal()).toFixed(2));


    const existingProduct = this.listProductos.find(producto => producto.getCodigo() === nuevoProducto.getCodigo());
    if (!existingProduct) {
      this.listProductos.push(nuevoProducto);
    }
    else {
      existingProduct.setCantidad(nuevoProducto.getCantidad());
    }
    this.productosForm.reset()
    this.producto = new Producto();
    Swal.fire({
      position: "top-end",
      icon: "success",
      title: "Producto agregado",
      showConfirmButton: false,
      timer: 1500
    });
  }

  validarStock($event: any) {
    if ($event.target.value >= this.stockProducto) {
      this.productosForm.get('cantidadProducto')?.setValue(this.stockProducto);
      console.log("el stock es ", this.stockProducto);
      this.productosForm.get('cantidadProducto')?.markAsTouched();
      this.productosForm.get('cantidadProducto')?.setErrors({ 'stockExcedido': true });
      this.hayStock = false;
      return;

    } else {
      this.productosForm.get('cantidadProducto')?.setErrors(null);
      this.hayStock = true;

    }

  }
  editProduct(index: number) {
    this.producto.codigo = this.listProductos[index].getCodigo();
    this.editar = false;
  }

  deleteProduct(index: number) {
    console.log(index);
    this.Total= this.Total-this.listProductos[index].getSubtotal();
    this.listProductos.splice(index, 1);
  }

  generarFactura(){
    if(this.listProductos.length!=0){
      this.facturaService.setListProductos(this.listProductos)
      this.facturaService.setTotal(this.Total)
      this.router.navigate(['cajero/factura']);
    }
  }

}