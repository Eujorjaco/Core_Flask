from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash

from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante

@app.route("/estudiante")
def estudiantes():
    cursos=Curso.get_all()
    return render_template("estudiante.html",todos_cursos=cursos)

@app.route("/iestudiante",methods=['POST'])
def iestudiante():
    data={
        "nombre":request.form['nombre'],
        "apellido":request.form['apellido'],
        "edad":request.form['edad'],
        "curso_id":request.form['curso_id']
    }
    Estudiante.save(data)
    return redirect("/cursos")