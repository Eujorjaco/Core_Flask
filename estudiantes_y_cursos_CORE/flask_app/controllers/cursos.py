from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash

from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante

@app.route("/cursos")
def cursos():
    cursos=Curso.get_all()
    return render_template("cursos.html",todos_cursos=cursos) 

@app.route("/icurso",methods=['POST'])
def icurso():
    data={
        "nombre":request.form['nombre']
    }
    Curso.save(data)
    return redirect("cursos")

@app.route("/cursos/<int:curso_id>")
def vercurso(curso_id):
    datos={
        'id': curso_id,
    }
    curso = Curso.get_estudiantes_cursos(datos)
    return render_template("vercurso.html",curso=curso)