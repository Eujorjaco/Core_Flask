from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import curso
from flask_app.models import estudiante

class Estudiante:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM estudiantes;"
        resultados = connectToMySQL('estudiantes_y_cursos').query_db(query)
        estudiantes = []
        for estudiante in resultados:
            estudiantes.append(cls(estudiante))
        return estudiantes
    
    @classmethod
    def get_one(cls, evento_id):
        query = "SELECT * FROM estudiantes WHERE id = %(id)s;"
        datos={"id":evento_id}
        resultado = connectToMySQL('estudiantes_y_cursos').query_db(query, datos)
        if resultado:
            return cls(resultado[0])
        return False
    
    @classmethod
    def save(cls, datos):
        query = """INSERT INTO estudiantes (nombre, apellido, edad, curso_id) 
                VALUES(%(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s );"""
        nuevo_id=connectToMySQL('estudiantes_y_cursos').query_db(query, datos)
        return nuevo_id
    
