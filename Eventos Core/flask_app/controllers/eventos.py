from flask_app import app #Importamos la app
from flask_app.models.evento import Evento
from flask_app.models.usuario import Usuario
from flask import render_template,redirect,request,session,flash

@app.route("/crear")
def crear():
    return render_template("nuevo.html")

@app.route("/creando",methods=['POST'])
def creando():
    if not Evento.validar_evento(request.form.to_dict()):
        return redirect("/eventos")
    datos={
        "evento":request.form['evento'],
        "ubicacion":request.form['ubicacion'],
        "fecha":request.form['fecha'],
        "descripcion":request.form['descripcion'],
        "usuario_id":request.form['usuario_id']
    }
    Evento.save(datos)
    flash("evento guardado")
    return redirect("/eventos")

@app.route("/ver/<int:evento_id>")
def mostrar_evento(evento_id):
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para acceder", "error")
        return redirect("/")
    datos={
        'id': evento_id,
    }
    usuario=Usuario.get_usuario_evento(datos)
    if not usuario:
        flash("Evento no encontrado", "error")
        return redirect("/eventos")
    return render_template("ver.html", usuario=usuario)

@app.route("/ver/editar/<int:evento_id>")
def editar(evento_id):
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para acceder", "error")
        return redirect("/")
    evento=Evento.get_one(evento_id)
    if not evento:
        return redirect("/eventos")
    return render_template("editar.html", evento=evento)

@app.route("/editando",methods=['POST'])
def editando():
    if not Evento.validar_evento(request.form.to_dict()):
        return redirect("/eventos")
    datos={
        "evento":request.form['evento'],
        "ubicacion":request.form['ubicacion'],
        "fecha":request.form['fecha'],
        "descripcion":request.form['descripcion'],
        "id":request.form['id']
    }
    Evento.update(datos)
    return redirect("/eventos")
    
@app.route("/ver/eliminar/<int:evento_id>",methods=['POST'])
def eliminar(evento_id):
    evento = Evento.get_one(evento_id)
    if evento:
    # Eliminamos el usuario
        Evento.delete(evento_id)
        # Redirigimos a la página principal
    return redirect('/eventos')