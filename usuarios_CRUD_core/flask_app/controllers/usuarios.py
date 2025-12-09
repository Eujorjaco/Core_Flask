from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash

from flask_app.models.usuario import Usuario

@app.route("/usuarios")
def usuarios():
    usuarios=Usuario.get_all()
    return render_template("usuarios.html",todos_usuarios=usuarios)

@app.route("/usuarios/nuevo")
def nuevo():
    return render_template("index.html")

@app.route("/crear",methods=['POST'])
def crear():
    datos={
        "usuario":request.form['nombre'],
        "apellido":request.form['apellido'],
        "email":request.form['email'],
    }
    Usuario.save(datos)
    return redirect("usuarios")

@app.route("/usuarios/<int:usuario_id>")
def ver(usuario_id):
    usuario=Usuario.get_one(usuario_id)
    return render_template("ver.html",usuario=usuario)

@app.route("/usuarios/editar/<int:usuario_id>")
def edicion(usuario_id):
    usuario=Usuario.get_one(usuario_id)
    return render_template("editar.html",usuario=usuario)

@app.route("/editar",methods=['POST'])
def editar():
    datos={
        "id":request.form['id'],
        "usuario":request.form['nombre'],
        "apellido":request.form['apellido'],
        "email":request.form['email']
    }
    print(datos)
    Usuario.update(datos)
    return redirect("/usuarios")

@app.route("/usuarios/eliminar/<int:usuario_id>",methods=['POST'])
def eliminar(usuario_id):
    usuario=Usuario.get_one(usuario_id)
    if usuario:
        Usuario.delete(usuario_id)
    return redirect("/usuarios")