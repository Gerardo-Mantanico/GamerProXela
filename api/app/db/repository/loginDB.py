class LoginDB():

   def ingresar(self, data):
            with self.conn.cursor() as cur:
                # Ejecutar la función almacenada y pasar parámetros de forma segura
                cur.execute(
                    "SELECT * FROM administrador.login(%s, %s)", 
                    (data['email'], data['password'])
                )
                # Obtener todos los resultados
                data = cur.fetchall()
                return data
        
        