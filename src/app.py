from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOUsuario import DAOUsuario
 

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = DAOUsuario()

ruta1 ='/alumno'
ruta2 = '/profesor'


@app.route('/registro')
def index():
    return render_template('registro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/nuevo_inicio', methods = ['POST'])
def ninicio():
    if request.method == 'POST'and request.form['registrar']:
        if db.create(request.form):
            if request.form['tipo'] == 'cliente':
                return redirect(url_for('cliente',usuario =request.form['usuario']))
            else:
                return redirect(url_for('productor',usuario =request.form['usuario']))
        else:
            flash("ERROR al crear usuario, emplee otro usuario")
            return render_template('registro.html')
    else:
        return render_template('registro.html')

@app.route('/iniciar', methods = ['POST'])
def iniciar():
    if request.method == 'POST'and request.form['iniciar']:
        data = db.validate(request.form)
        if len(data) != 0:
            if data[5] == 'cliente':
                return redirect(url_for('cliente',usuario = data[2]))
            else:
                return redirect(url_for('productor',usuario = data[2]))
        else:
            flash("ERROR, usuario invalido")
            return redirect(url_for('ninicio'))
    else:
        return render_template('login.html')

@app.route('/productor/<usuario>')
def productor(usuario):
    data = db.sesion(usuario)
    return render_template('productor/productor_index.html', data = data) 

@app.route('/cliente/<usuario>')
def cliente(usuario): 
    return render_template('cliente/tienda.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0",debug=True)
