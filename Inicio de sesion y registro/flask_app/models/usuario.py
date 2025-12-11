from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL('usuario_registro').query_db(query)
        usuarios = []
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios
    
    @classmethod
    def get_one(cls, evento_id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        datos={"id":evento_id}
        resultado = connectToMySQL('usuario_registro').query_db(query, datos)
        if resultado:
            return cls(resultado[0])
        return False
    
    @classmethod
    def save(cls, datos):
        query = """INSERT INTO usuarios (nombre, apellido, email,password) 
                VALUES(%(nombre)s, %(apellido)s, %(email)s,%(password)s);"""
        nuevo_id=connectToMySQL('usuario_registro').query_db(query, datos)
        return nuevo_id
    
    @classmethod
    def buscar_por_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %(email)s"
        resultado = connectToMySQL('usuario_registro').query_db(query, {'email': email})
        if len(resultado) > 0:
            return cls(resultado[0])  # Retorna el usuario encontrado
        return None  # No existe
    

    @staticmethod
    def validar_usuario(data):
        es_valido = True
        if len(data['nombre']) < 3:
            flash("El nombre debe tener al menos 2 caracteres")
            es_valido = False 
        if len(data['apellido']) < 3:
            flash("El apellido debe tener al menos 2 caracteres")
            es_valido = False 
        if len(data['email'].strip()) == 0:
            flash("El email es obligatorio", "email")
            es_valido = False
        elif not EMAIL_REGEX.match(data['email']):
            flash("E-mail inválido. Debe tener formato válido (ejemplo@dominio.com)", "email")
            es_valido = False
        elif Usuario.buscar_por_email(data['email']):
            flash("Este email ya está registrado. Por favor use otro email.", "email")
            es_valido = False
        if len(data.get('password', '').strip()) == 0:
            flash("La contraseña es obligatoria", "password")
            es_valido = False
        elif len(data['password'].strip()) < 8:
            flash("La contraseña debe tener al menos 8 caracteres", "password")
            es_valido = False
        if 'confirm_password' in data:
            if data['password'] != data['confirm_password']:
                flash("Las contraseñas no coinciden", "password")
                es_valido = False
        return es_valido