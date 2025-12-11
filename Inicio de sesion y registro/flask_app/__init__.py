from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__) #Crea instancia de Flask
app.secret_key = "clave secreta, shhhh!"

bcrypt = Bcrypt(app) 