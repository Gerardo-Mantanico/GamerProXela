import { Time } from "@angular/common";
export class Empleado{
    constructor(
        private id: number,
        private rol: string,
        private usuario: string,
        private password: string,
        private id_sucursal: number,
        private nombre: string,
        private telefono: number,
        private correo: string
    )
    {}

public getId(){
    return this.id
}


public getNombre(){
    return this.nombre
}


public getRol(){
    return this.rol
}
}