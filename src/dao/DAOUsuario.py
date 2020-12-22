import pymysql

class DAOUsuario:
    def connect(self):
        return pymysql.connect("localhost","root","","db_chaka" )

    def validate(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("select * from usuario where correo = %s and clave = %s",(data['correo'],data['clave'],))
            return cursor.fetchone()
        except:
            return ()
        finally:
            con.close()

    def create(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO usuario(nombre,usuario,correo,clave,tipo) VALUES(%s, %s, %s, %s, %s)", (data['nombre'],data['usuario'],data['correo'],data['clave'],data['tipo'],)) 
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
    
    def sesion(self,user):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("select * from usuario where usuario = %s",(user,))
            return cursor.fetchone()
        except:
            return ()
        finally:
            con.close()   

class DAOProducto:
    def connect(self):
        return pymysql.connect("localhost","root","","db_chaka" )

    def read(self, id):
        con = DAOProducto.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM producto order by nombre asc")
            else:
                cursor.execute("SELECT * FROM producto where idproducto = %s order by titulo asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOProducto.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO producto(idproductor,categoria,precio,stock,descripcion,valoracion,imagen,titulo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (data['idproductor'],data['categoria'],data['precio'],data['stock'],data['descripcion'],data['valoracion'],data['imagen'],data['titulo']))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = DAOProducto.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE producto set idproductor = %s, categoria = %s, precio = %s , stock = %s , descripcion = %s, valoracion = %s, imagen = %s, titulo = %s where idproducto = %s", (data['idproductor'],data['categoria'],data['precio'],data['stock'],data['descripcion'],data['valoracion'],data['imagen'],data['titulo'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = DAOProducto.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM producto where idproducto = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()     
