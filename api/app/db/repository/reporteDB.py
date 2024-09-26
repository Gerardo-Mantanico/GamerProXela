class ReporteDB():
    
    def obtener_top_ventas_grandes(self, fecha):
        inicio = fecha['inicio']
        final = fecha['final']
        
        with self.conn.cursor() as cur:
            cur.execute("""
                        SELECT * FROM administrador.ventas_grandes
                        WHERE fecha_emision BETWEEN %s  AND  %s   AND nit NOT IN ('CF', 'cf')
                        ORDER BY total DESC
                        LIMIT 10
            """, (inicio, final))
            datas = cur.fetchall()
            result = []  
            for data in datas:
                dictionary = {
                    "no_factura": data[0],
                    "sucursal": data[1],
                    "nit": data[2],
                    "nombre": data[3],
                    "fecha": data[4],
                    "total": data[5]
                }
                result.append(dictionary) 
        return result  
    


    def historial(self, fecha):
        inicio = fecha['inicio']
        final = fecha['final']
        with self.conn.cursor() as cur:
            cur.execute("""
                        SELECT h.*, cf.numero_factura, cf.total  FROM administrador.historial_descuentos h
                        INNER JOIN cajero.factura cf ON cf.id_factura= h.id_factura
                        WHERE fecha BETWEEN  %s  AND  %s 

                     """, (inicio, final))
            datas = cur.fetchall()
            result = []  
            for data in datas:
                dictionary = {
                    "no_factura": data[4],
                    "monto": data[3],
                    "fecha": data[2],
                    "total": data[5]
                }
                result.append(dictionary) 
        return result  
    


    def obtener_top_sucursales_ingreso(self):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM administrador.top_sucursales_ingreso
                """
            )
            datas = cur.fetchall()  
            result = []  
            for data in datas:
                dictionary = {
                    "nombre": data[0],
                    "direccion": data[1],
                    "hora_apertura": data[2],
                    "hora_cierre": data[3],
                    "total": data[4]
                }
                result.append(dictionary) 
        return result  



    

    def obtener_top_articulos_vendidos(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM administrador.top_articulos_vendidos
            """)
            datos = cur.fetchall()  
            arreglo_producto = []
            for data in datos:  
                dictionary = {
                    "nombre": data[0],
                    "cantidad": data[1],
                }
                arreglo_producto.append(dictionary)
            
            return arreglo_producto



    def obtener_top_clientes_gastadores(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                        SELECT * FROM administrador.top_clientes_gastadores
                        """)
            datos = cur.fetchall()

            arreglo_clientes = []
            for data in datos:
                cliente = {
                    "id": data[0],
                    "nombre": data[1],
                    "nit": data[2],
                    "telefono": data[3],
                    "direccion": data[4],
                    "total": data[5],
                }
                arreglo_clientes.append(cliente)
            
            return arreglo_clientes


 
