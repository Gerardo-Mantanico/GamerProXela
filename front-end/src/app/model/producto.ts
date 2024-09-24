export class Producto {
    public codigo!: string;
    public descripcion!: string;
    public descripcion_pasillo!: string[];
    public existencia!: number;
    public id_producto!: number;
    public id_productoEstanteria!: number;
    public no_pasillo!: number[];
    public nombre!: string;
    public precio!: string;
    public categoria! :string;

  

    getcategoria(): string{
         return this.categoria
    } 
   
    // Métodos get
    getcodigo(): string {
            return this.codigo;
    }

    getdescripcion(): string {
        return this.descripcion;
    }

    getdescripcionPasillo(): string[] {
        return this.descripcion_pasillo;
    }

    getexistencia(): number {
        return this.existencia;
    }

    getidProducto(): number {
        return this.id_producto;
    }

    getidProductoEstanteria(): number {
        return this.id_productoEstanteria;
    }

    getnoPasillo(): number[] {
        return this.no_pasillo;
    }

    getnombre(): string {
        return this.nombre;
    }

    getprecio(): string {
        return this.precio;
    }

    // Métodos set
    setcodigo(codigo: string) {
        this.codigo = codigo.trim();
    }

    setdescripcion(descripcion: string) {
        this.descripcion = descripcion.trim();
    }

    setdescripcionPasillo(descripcionPasillo: string[]) {
        this.descripcion_pasillo = descripcionPasillo;
    }

    setexistencia(existencia: number) {
        this.existencia = existencia;
    }

    setidProducto(idProducto: number) {
        this.id_producto = idProducto;
    }

    setidProductoEstanteria(idProductoEstanteria: number) {
        this.id_productoEstanteria = idProductoEstanteria;
    }

    setnoPasillo(noPasillo: number[]) {
        this.no_pasillo = noPasillo;
    }

    setnombre(nombre: string) {
        this.nombre = nombre.trim();
    }

    setprecio(precio: string) {
        this.precio = precio.trim();
    }
    setcategoria(categoria: string){
        this.categoria=categoria.trim();
    }
    
}

