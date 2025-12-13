from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 

class Evento:
    def __init__(self, data):
        self.id = data['id']
        self.evento = data['evento']
        self.ubicacion = data['ubicacion']
        self.fecha = data['fecha']
        self.descripcion = data['descripcion']
        self.usuario_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.id_nombre = data.get('id_nombre',"") #caja vacia para poner nombre por la id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM eventos;"
        resultados = connectToMySQL('usuario_registro').query_db(query)
        usuarios = []
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios
    
    @classmethod
    def get_one(cls, evento_id):
        query = "SELECT * FROM eventos WHERE id = %(id)s;"
        datos={"id":evento_id}
        resultado = connectToMySQL('eventos_core').query_db(query, datos)
        if resultado:
            return cls(resultado[0])
        return False
    
    @classmethod
    def save(cls, datos):
        query = """INSERT INTO eventos (evento, ubicacion, fecha,descripcion,usuario_id) 
                VALUES(%(evento)s, %(ubicacion)s, %(fecha)s,%(descripcion)s,%(usuario_id)s);"""
        nuevo_id=connectToMySQL('eventos_core').query_db(query, datos)
        return nuevo_id
    
    @classmethod
    def update(cls, datos):
        query = "UPDATE eventos SET evento=%(evento)s, ubicacion=%(ubicacion)s, fecha=%(fecha)s, descripcion=%(descripcion)s WHERE id = %(id)s;"
        return connectToMySQL('eventos_core').query_db(query, datos)

    @classmethod
    def delete(cls, evento_id):
        query = "DELETE FROM eventos WHERE id = %(id)s;"
        datos = {
            'id':evento_id
        }
        return connectToMySQL('eventos_core').query_db(query, datos)

    @staticmethod
    def validar_evento(data):
        es_valido=True
        if len(data['evento'])<3:
            flash("Evento debe tener mas de 3 letras")
            es_valido=False
        if len(data['ubicacion'])<3:
            flash("Ubicacion debe tener mas de 3 letras")
            es_valido=False
        if len(data['descripcion'])<3:
            flash("Descripcion debe tener mas de 3 letras")
            es_valido=False
        return es_valido