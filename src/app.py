from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOUsuario import DAOUsuario, DAOProducto
 

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = DAOUsuario()
dbProducto = DAOProducto()

@app.route('/registro')
def index():
    return render_template('registro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/productor/contacto/<string:usuario>')
def contactanos(usuario):
    user = db.sesion(usuario)  
    return render_template('productor/contactanos.html', user = user)

@app.route('/nuevo_inicio', methods = ['POST', 'GET'])
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
        if data == None:
            flash("ERROR, usuario invalido")
            return redirect(url_for('ninicio'))
        else:    
            if len(data) != 0:
                if data[5] == 'cliente':
                    return redirect(url_for('cliente',usuario = data[2]))
                else:
                    return redirect(url_for('productor',usuario = data[2]))                
    else:
        return render_template('login.html')

@app.route('/productor/<string:usuario>')
def productor(usuario):
    user = db.sesion(usuario)
    stock = dbProducto.stock(user[0])
    productos = dbProducto.readProductor(user[0])
    """db.sesion es una funcion para conocer el usuario que esta conectado"""                                               
    return render_template('productor/productor_index.html', user = user, stock = stock, productos = productos) 

@app.route('/productor/producto/<string:usuario>')
def productor_producto(usuario):
    print(usuario)
    user = db.sesion(usuario)
    data = dbProducto.readProductor(user[0])
    return render_template('productor/productos.html', data = data, user = user)

@app.route('/productor/add/<string:usuario>')
def productor_add(usuario):
    user = db.sesion(usuario)
    data = dbProducto.readProductor(user[0])
    return render_template('productor/add.html', data = data, user = user)

@app.route('/productor/update/<string:usuario>/<int:producto>')
def producto_update(usuario,producto):
    user = db.sesion(usuario)
    data = dbProducto.read(producto)
    return render_template('productor/update.html', data = data, user = user)

@app.route('/productor/anadirProducto/<string:usuario>', methods = ['POST', 'GET'])
def anadirProducto(usuario):
    user = db.sesion(usuario)
    if request.method == 'POST' and request.form['guardar']:
        if dbProducto.insert(request.form):
            print(request.form)
            flash("Nuevo producto creado")
        else:
            flash("ERROR, al crear producto")

        return redirect(url_for('productor_add', usuario = user[2]))
    else:
        return redirect(url_for('productor_add', usuario = user[2]))

@app.route('/productor/update_lista/<string:usuario>/<int:producto>', methods = ['POST', 'GET'])
def producto_update_lista(usuario,producto):
    user = db.sesion(usuario)
    if request.method == 'POST' and request.form['update']:
        print(request.form)
        print(producto)
        if dbProducto.update(producto,request.form):
            flash("Nuevo producto creado")
        else:
            flash("ERROR, al crear producto")

        return redirect(url_for('productor_producto', usuario = user[2]))
    else:
        return redirect(url_for('productor_producto', usuario = user[2]))

@app.route('/productor/delete/<string:usuario>/<int:producto>')
def eliminarProducto(usuario,producto):
    user = db.sesion(usuario)
    print(producto)
    dbProducto.delete(producto)
    return redirect(url_for('productor_producto', usuario = user[2]))


@app.route('/cliente/<usuario>')
def cliente(usuario): 
    return render_template('cliente/tienda.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0",debug=True)
