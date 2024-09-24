import { ProductoFactura } from "./productoFactura";

export class Factura{
    
    constructor(
        private id_cliente: number,
        private nit: string,
        private nombre: string,
        private direccion: string,
        private telefono: number,
        private id_sucursal: number,
        private id_cajero: number,
        private total: number,
        private descuento: number,
        private listProduct: ProductoFactura[] = [] // Cambia `any` por el tipo adecuado
    ) {}

    // Getters
    getIdCliente(): number {
        return this.id_cliente;
    }

    getNit(): string {
        return this.nit;
    }

    getNombre(): string {
        return this.nombre;
    }

    getDireccion(): string {
        return this.direccion;
    }

    getTelefono(): number {
        return this.telefono;
    }

    getIdSucursal(): number {
        return this.id_sucursal;
    }

    getIdCajero(): number {
        return this.id_cajero;
    }

    getTotal(): number {
        return this.total;
    }

    getDescuento(): number {
        return this.descuento;
    }

    getProductoFactura(): any[] {
        return this.listProduct;
    }

    // Setters
    setNit(nit: string): void {
        this.nit = nit;
    }

    setNombre(nombre: string): void {
        this.nombre = nombre;
    }

    setDireccion(direccion: string): void {
        this.direccion = direccion;
    }

    setTelefono(telefono: number): void {
        this.telefono = telefono;
    }

    setIdSucursal(id_sucursal: number): void {
        this.id_sucursal = id_sucursal;
    }

    setIdCajero(id_cajero: number): void {
        this.id_cajero = id_cajero;
    }

    setTotal(total: number): void {
        this.total = total;
    }

    setDescuento(descuento: number): void {
        this.descuento = descuento;
    }

    setProductoFactura(productoFactura: ProductoFactura[]): void {
        this.listProduct = productoFactura;
    }
}