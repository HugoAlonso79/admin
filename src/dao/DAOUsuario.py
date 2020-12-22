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
