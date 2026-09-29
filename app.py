from flask import Flask, render_template, request, redirect, flash
from usuarios import Usuario

app = Flask(__name__)

app.secret_key = "clave_simple_para_la_aplicacion"


@app.route("/")
def inicio():
    usuarios = Usuario.todos()
    return render_template("index.html", usuarios=usuarios)


@app.route("/usuario_nuevo")
def nuevo_usuario():
    return render_template("registro.html")


@app.route("/Crear", methods=["POST"])
def crear_usuario():

    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    email = request.form.get("email")

    if not nombre or not apellido or not email:
        flash("Debes completar todos los campos.", "error")
        return redirect("/usuario_nuevo")

    datos = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email
    }

    Usuario.crear(datos)

    flash("Usuario creado correctamente.", "success")

    return redirect("/")


@app.route("/usuario/<int:user_id>")
def mostrar_usuario(user_id):

    usuario = Usuario.buscar_por_id(user_id)

    if usuario is None:
        flash("El usuario no existe.", "error")
        return redirect("/")

    return render_template("usuario.html", usuario=usuario)


@app.route("/editar/<int:user_id>")
def formulario_edicion(user_id):

    usuario = Usuario.buscar_por_id(user_id)

    if usuario is None:
        flash("El usuario no existe.", "error")
        return redirect("/")

    return render_template("edicion.html", usuario=usuario)


@app.route("/Editar/<int:user_id>", methods=["POST"])
def actualizar_usuario(user_id):

    datos = {
        "id": user_id,
        "nombre": request.form.get("nombre"),
        "apellido": request.form.get("apellido"),
        "email": request.form.get("email")
    }

    Usuario.actualizar(datos)

    flash("Usuario actualizado correctamente.", "success")

    return redirect(f"/usuario/{user_id}")


@app.route("/borrar/<int:user_id>")
def borrar_usuario(user_id):

    Usuario.eliminar(user_id)

    flash("Usuario eliminado correctamente.", "success")

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)