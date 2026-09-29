from mysqlconnector import conectar 

BASE_DE_DATOS = "usuarios_crud"


Class Usuario:

def __init__(self, datos):

    self.id = datos["id"]
    self.nombre = datos["nombre"]
    self.apellido = datos["apellido"]   
    self.email = datos["email"]
    self.created_at = datos["created_at"]
    self.updated_at = datos["updated_at"]



 @classmethod
    def todos(cls):

        consulta = """
            SELECT *
            FROM usuarios
            ORDER BY id DESC
        """

        resultados = conectar(
            BASE_DATOS
        ).query_db(consulta)

        usuarios = []

        if resultados:

            for datos in resultados:

                usuarios.append(
                    cls(datos)
                )

        return usuarios


    @classmethod
    def buscar_por_id(cls, usuario_id):

        consulta = """
            SELECT *
            FROM usuarios
            WHERE id = %(id)s
        """

        datos = {
            "id": usuario_id
        }

        resultado = conectar(
            BASE_DATOS
        ).query_db(
            consulta,
            datos
        )

        if not resultado:

            return None

        return cls(resultado[0])


    
     @classmethod
    def crear(cls, datos):

        consulta = """
            INSERT INTO usuarios
            (nombre, apellido, email)
            VALUES
            (%(nombre)s, %(apellido)s, %(email)s)
        """

        resultado = conectar(
            BASE_DATOS
        ).query_db(
            consulta,
            datos
        )

        return resultado



@classmethod
    def actualizar(cls, datos):

        consulta = """
            UPDATE usuarios
            SET
                nombre = %(nombre)s,
                apellido = %(apellido)s,
                email = %(email)s
            WHERE id = %(id)s
        """

        return conectar(
            BASE_DATOS
        ).query_db(
            consulta,
            datos
        )



@classmethod
    def eliminar(cls, usuario_id):

        consulta = """
            DELETE FROM usuarios
            WHERE id = %(id)s
        """

        datos = {
            "id": usuario_id
        }

        return conectar(
            BASE_DATOS
        ).query_db(
            consulta,
            datos
        )

