import { Time } from "@angular/common"

export class Sucursal {
    constructor(
        private id_sucural: number,
        private direccion: string,
        private nombre: string,
        private no_sucursal: number,
        private codigo: string,
        private correo:string,
        private telefono: number,
        private horario_apertura: string,
        private horario_cierre: string
    )
    {}
}
