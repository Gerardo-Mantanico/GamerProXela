class ProductosEstanteriaDB():
     
    def insert(self, data):
        with self.conn.cursor() as cur:
            cur.execute(
                """
               CALL inventario.insertar_productos_estanteria(%(id_estanteria)s, %(id_producto)s, %(cantidad)s, %(id_pasillo)s)
                """,data,
            )
            self.conn.commit()


    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute(
            """
                        DELETE FROM inventario.estanteria_producto  WHERE id_estanteria_producto=%s
                        """,
            (id,),
        )
        self.conn.commit()


    def update_product(self, data):
        with self.conn.cursor() as cur:
            cur.execute(
            """
                        UPDATE inventario.estanteria_producto
	                    SET  id_estanteria=%(id_estanteria)s, id_producto_bodega=%(id_producto_bodega)s, no_pasillo=%(no_pasillo)s
	                    WHERE id_estanteria_producto=%(id_estanteria_producto)s
                            """,
            data,
        )
        self.conn.commit()



    def list_product(self, id):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                    SELECT *  FROM inventario.producto_estanteria WHERE id_estanteria=%s
                """,(id,)
            )
            data = []
            data = cur.fetchall()
            productos = []
            for row in  data:
                    producto = {
                        "id_producto_estanteria": row[0],
                        "id_producto": row[1],
                        "codigo": row[2],
                        "nombre": row[3],
                        "descripcion": row[4],
                        "precio": row[5],
                        "categoria": row[6],
                        "no_pasillo": row[8],
                        "descripcion_pasillo": row[9],
                        "existencia": row[7],
                    }
                    productos.append(producto)
        return {"productos": productos}
    

    def list_product_estanteria(self, data):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                    SELECT * 
                    FROM inventario.producto_estanteria 
                    WHERE id_sucursal = %(id_sucursal)s 
                    AND LOWER(codigo_producto) = LOWER( %(codigo_producto)s) 
                    OR LOWER(nombre) = LOWER(%(nombre)s)
                   
               """,data,
            )

            data = cur.fetchone()
            categoria = "Consola" if data[6] == 1 else "Videojuego"
            mapped_data = {
                "id_productoEstanteria": data[0],
                "id_producto": data[1],
                "codigo": data[2].strip(),  # Eliminar espacios en blanco
                "nombre": data[3].strip(),
                "descripcion": data[4].strip(),
                "precio": data[5].strip(),
                "categoria": categoria,
                "existencia": data[7],
                "no_pasillo": data[8],
                "descripcion_pasillo": data[9],

            }
            return mapped_data
        
      
     
     
     
   
 
    
  

    

        
    
          