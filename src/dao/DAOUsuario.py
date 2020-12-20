import pymysql

class DAOUsuario:
    def connect(self):
        return pymysql.connect("localhost","root","","db_poo" )

    def validate(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("select * from usuario where usuario = %s and clave = %s",(data['usuario'],data['clave'],))
            return cursor.fetchone()
        except:
            return ()
        finally:
            con.close()

    def create(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO usuario(nombre,usuario,clave,tipo) VALUES(%s, %s, %s,%s)", (data['nombre'],data['usuario'],data['clave'],data['tipo'],)) 
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
