import datetime
import hashlib
from usuarios import conexion as conexion

connect = conexion.conectar()
db = connect[0]
cursor = connect[1]



class User:
    def __init__(self, nombre, apellido, email, psw) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.psw = psw
    def signup(self):
        fecha = datetime.datetime.now()

        # Cifrar Pass
        cifrado = hashlib.sha256()
        cifrado.update(self.psw.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, user)
            db.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
    
        return result

    def identificar(self):
        
        # Comprobar si existe usr
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        
        # Cifrar Pass
        cifrado = hashlib.sha256()
        cifrado.update(self.psw.encode('utf8'))

        # Data consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result
