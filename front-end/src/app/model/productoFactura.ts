export class ProductoFactura {
    private codigo!: string;
    private nombre!: string;
    private cantidad!: number;
    private precio!: string;
    private subtotal!: number
    private subtotalDescuento!: number



  getCodigo(): string {
    return this.codigo;
  }

  setCodigo(codigo: string): void {
    this.codigo = codigo;
  }


  getNombre(): string {
    return this.nombre;
  }

  setNombre(nombre: string): void {
    this.nombre = nombre;
  }


  getCantidad(): number {
    return this.cantidad;
  }

  setCantidad(cantidad: number): void {
    this.cantidad = cantidad;
  }


  getPrecio(): string {
    return this.precio;
  }

  setPrecio(precio: string): void {
    this.precio = precio;
  }


  getSubtotal(): number {
    return this.subtotal;
  }

  setSubtotal(subtotal: number): void {
    this.subtotal = subtotal;
  }

  getSubtotalDescuento(): number {
    return this.subtotalDescuento;
  }

  setSubtotalDescuento(subtotalDescuento: number): void {
    this.subtotalDescuento = subtotalDescuento;
  }

}