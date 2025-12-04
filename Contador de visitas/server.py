from flask import Flask, render_template , request, redirect, session

app = Flask(__name__)

app.secret_key = '123456'


@app.route('/')
def contar_visitas():
    if 'borrados' not in session:
        session['borrados'] =0
    if 'visitas' in session:
        session['visitas'] +=1
    else:
        session['visitas']=0
    return render_template("visit.html",visita=session['visitas'],borrado=session['borrados'])

@app.route('/aumenta2',methods=['POST'])
def aumenta2():
    session['visitas'] +=1
    return redirect('/')

@app.route('/aumentax',methods=['POST'])
def aumentax():
    session['visitas'] =session['visitas']+int(request.form['number'])-1
    return redirect('/')

@app.route('/borrar_visitas',methods=['POST'])
def borrar_visitas():
    if 'borrados' in session:
        session['borrados'] +=1
    session['visitas']=-1
    return redirect('/')

@app.route('/destruir_sesion')
def formatear():
    session.clear()
    return redirect ('/')

if __name__ == "__main__":

    app.run(debug=True)
