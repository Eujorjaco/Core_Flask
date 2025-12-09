from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['usuario']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL('esquema_usuarios').query_db(query)
        usuarios = []
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios
    
    @classmethod
    def get_one(cls, evento_id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        datos={"id":evento_id}
        resultado = connectToMySQL('esquema_usuarios').query_db(query, datos)
        if resultado:
            return cls(resultado[0])
        return False


    @classmethod
    def save(cls, datos):
        query = """INSERT INTO usuarios (usuario, apellido, email) 
                VALUES(%(usuario)s, %(apellido)s, %(email)s);"""
        nuevo_id=connectToMySQL('esquema_usuarios').query_db(query, datos)
        return nuevo_id
    
    @classmethod
    def update(cls, datos):
        query = """UPDATE usuarios 
            SET usuario = %(usuario)s, 
            apellido = %(apellido)s, 
            email = %(email)s, 
            updated_at = NOW()
            WHERE id = %(id)s;
        """
        return connectToMySQL('esquema_usuarios').query_db(query, datos)
    
    @classmethod
    def delete(cls, usuario_id):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        datos = {
        'id': usuario_id
        }
        return connectToMySQL('esquema_usuarios').query_db(query, datos)