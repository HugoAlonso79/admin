from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOUsuario import DAOUsuario
 

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = DAOUsuario()

ruta1 ='/alumno'
ruta2 = '/profesor'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/nuevo_inicio', methods = ['POST'])
def ninicio():
    if request.method == 'POST'and request.form['registrar']:
        if db.create(request.form):
            flash("Registrado correctamente")
            if request.form['tipo'] == 'profesor':
                return redirect(url_for('profesor'))
            else:
                return redirect(url_for('alumno'))
        else:
            flash("ERROR, al crear usuario")
            return render_template('login.html')
    else:
        return render_template('index.html')

@app.route('/iniciar', methods = ['POST'])
def iniciar():
    if request.method == 'POST'and request.form['iniciar']:
        data = db.validate(request.form)
        if len(data) != 0:
            if data[4] == 'alumno':
                return redirect(url_for('alumno'))
            else:
                return redirect(url_for('profesor'))
        else:
            flash("ERROR, usuario invalido")
            return redirect(url_for('ninicio'))
    else:
        return render_template('index.html')

@app.route(ruta1)
def alumno():
    return render_template('alumno/alumno.html')

@app.route(ruta1+'/notas')
def notas():
    return render_template('alumno/notas.html')

@app.route(ruta1+'/horario')
def horario():
    return render_template('alumno/horario.html')

@app.route(ruta2)
def profesor():
    return render_template('profesor/profesor.html')

@app.route(ruta2+'/registro')
def registro():
    return render_template('profesor/registro.html')

@app.route(ruta2+'/asistencia')
def asistencia():
    return render_template('profesor/asistencia.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0",debug=True)
