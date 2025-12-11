from flask_app import app #Importamos la app
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 
from flask import render_template,redirect,request,session,flash

@app.route("/")
def index():
    if 'usuario_id' in session:
        return redirect("/inicio")
    return render_template("index.html")

@app.route("/registro", methods=['POST'])
def registro():
    if not Usuario.validar_usuario(request.form.to_dict()):
        return redirect("/")
    pass_hasheado = bcrypt.generate_password_hash(request.form['password'])
    datos={
        "nombre":request.form['nombre'],
        "apellido":request.form['apellido'],
        "email":request.form['email'],
        "password":pass_hasheado,
        "confirm_password":request.form['confirm_password']
    }

    nuevo_id = Usuario.save(datos)
    session['usuario_id'] = nuevo_id
    return redirect("/inicio")

@app.route("/iniciar",methods=['POST'])
def iniciar():
    usuario = Usuario.buscar_por_email(request.form['email'])

    if not usuario:
        flash("E-mail no registrado", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("Contraseña incorrecta", "login")
        return redirect("/")
    session['usuario_id'] = usuario.id
    return redirect("/inicio")

@app.route("/inicio")
def inicio():
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para acceder", "error")
        return redirect("/")
    usuario = Usuario.get_one(session['usuario_id'])
    if not usuario:
        session.clear()
        flash("Usuario no encontrado", "error")
        return redirect("/")
    return render_template("inicio.html",usuario=usuario)

@app.route("/cerrar")
def cerrar():
    session.clear()
    flash("Sesión cerrada correctamente", "exito")
    return redirect("/")