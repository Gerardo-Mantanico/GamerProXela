import psycopg # type: ignore
class Connection():
    conn = None
    def __init__(self):
        try:
             self.conn= psycopg.connect(
                """
                    dbname=VentasControl
                    user=postgres
                    password=root
                    host=localhost
                    port=5432
                """
             )
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close

    def get_connection(self):
        if self.conn is None:
            raise Exception("No se pudo conectar a la base de datos")
        return self.conn        





    def __del__(self):
             self.conn.close