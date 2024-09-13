class UsuarioDB:

    # Este metodo se encarga de registrar una sucursal
    def register_user(self, data):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                            INSERT INTO administrador.empleado(
                            rol, usuario, contrasena, id_sucursal, nombre, telefono, correo)
                            VALUES (%(rol)s, %(usuario)s, %(password)s, %(id_sucursal)s, %(nombre)s, %(telefono)s, %(correo)s)
                            """,
                data,
            )
            self.conn.commit()


    def register_caja(self, data):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                            INSERT INTO administrador.cajero(
                            rol, usuario, contrasena, id_sucursal, nombre, telefono, correo,no_caja)
                            VALUES (%(rol)s, %(usuario)s, %(password)s, %(id_sucursal)s, %(nombre)s, %(telefono)s, %(correo)s, %(no_caja)s)
                            """,
                data,
            )
            self.conn.commit()
        
    def see_user(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute(
                """
                    SELECT * FROM administrador.empleado WHERE id_empleado=%s
                """,(id,),
            )
            return data.fetchone()


    def delete_user(self, id):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                 DELETE  FROM administrador.empleado WHERE id_empleado=%s
                """,(id,),
            )
            self.conn.commit()    
            
