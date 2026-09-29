import pymysql


class ConexionMySQL:

    def __init__(self, base_datos):

        self.conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database=base_datos,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )


    def query_db(self, consulta, datos=None):

        cursor = self.conexion.cursor()

        try:

            cursor.execute(
                consulta,
                datos
            )

            if consulta.strip().lower().startswith("select"):

                return cursor.fetchall()


            self.conexion.commit()

            if consulta.strip().lower().startswith("insert"):

                return cursor.lastrowid

            return True

        except Exception as error:

            print(
                "Error en la base de datos:",
                error
            )

            self.conexion.rollback()

            return False

        finally:

            cursor.close()
            self.conexion.close()


def conectar(base_datos):

    return ConexionMySQL(base_datos)