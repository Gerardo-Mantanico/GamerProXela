import { ProductoFactura } from "./productoFactura";

export class Factura{
    
    constructor(
        private id_cliente: number,
        private id_sucursal: number,
        private id_cajero: number,
        private total: string,
        private descuento: string,
        private listProduct: ProductoFactura[]
    ) {}

    // Getters
    getIdCliente(): number {
        return this.id_cliente;
    }

   

    getIdSucursal(): number {
        return this.id_sucursal;
    }

    getIdCajero(): number {
        return this.id_cajero;
    }

    getTotal(): string {
        return this.total;
    }

    getDescuento(): string {
        return this.descuento;
    }

    getProductoFactura(): any[] {
        return this.listProduct;
    }

    
    setIdSucursal(id_sucursal: number): void {
        this.id_sucursal = id_sucursal;
    }

    setIdCajero(id_cajero: number): void {
        this.id_cajero = id_cajero;
    }

    setTotal(total: string): void {
        this.total = total;
    }

    setDescuento(descuento: string): void {
        this.descuento = descuento;
    }

    setProductoFactura(productoFactura: ProductoFactura[]): void {
        this.listProduct = productoFactura;
    }
}