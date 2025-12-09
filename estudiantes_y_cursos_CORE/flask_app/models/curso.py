from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import estudiante
from pprint import pprint
class Curso:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.estudiantes=[]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursos;"
        resultados = connectToMySQL('estudiantes_y_cursos').query_db(query)
        cursos = []
        for curso in resultados:
            cursos.append(cls(curso))
        return cursos
    
    @classmethod
    def get_one(cls, evento_id):
        query = "SELECT * FROM cursos WHERE id = %(id)s;"
        datos={"id":evento_id}
        resultado = connectToMySQL('estudiantes_y_cursos').query_db(query, datos)
        if resultado:
            return cls(resultado[0])
        return False
    
    @classmethod
    def save(cls, datos):
        query = """INSERT INTO cursos (nombre) 
                VALUES(%(nombre)s);"""
        nuevo_id=connectToMySQL('estudiantes_y_cursos').query_db(query, datos)
        return nuevo_id
    
    @classmethod
    def get_estudiantes_cursos(cls,datos):
        query = """
            SELECT * FROM cursos
            LEFT JOIN estudiantes ON estudiantes.curso_id = cursos.id
            WHERE curso_id = %(id)s;        
        """
        resultados = connectToMySQL('estudiantes_y_cursos').query_db(query,datos)
        curso = cls(resultados[0])

        for fila in resultados:
            if fila['estudiantes.id']:
                datos_estudiante = {
                    "id": fila['estudiantes.id'],
                    "nombre": fila['estudiantes.nombre'],
                    "apellido": fila['apellido'],
                    "edad": fila['edad'],
                    "curso_id": fila['curso_id'],
                    "created_at": fila['estudiantes.created_at'],  #  tabla.columna
                    "updated_at": fila['estudiantes.updated_at'],
                }
            curso.estudiantes.append(estudiante.Estudiante(datos_estudiante))
            pprint(curso.estudiantes)
        return curso
