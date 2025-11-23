from flask import Flask , render_template, session, request, redirect

app = Flask(__name__) 

app.secret_key = 'ssclave'

@app.route("/")
def funcion():
    return render_template('index.html')

@app.route("/enviar", methods=['POST'])
def enviar():
    session["nombre"]=request.form["nombre"]
    session["lugar"]=request.form["lugar"]
    session["numero"]=request.form["numero"]
    session["comida"]=request.form["comida"]
    print(session)
    return redirect("/futuro")

@app.route("/futuro")
def futuro():
    return render_template("lectura.html",info=session)

if __name__=="__main__":
    app.run(debug=True)