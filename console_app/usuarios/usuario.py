import datetime
import hashlib
import usuarios.connection as conn

c = conn.connect()
database = c[0]
cursor = c[1]

class Usuario:

    def __init__(self, name, last_name, email, password) -> None:
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password

    def register(self):
        date = datetime.datetime.now()
        
        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = 'INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)'
        usuario = (self.name, self.last_name, self.email, cifrado.hexdigest(), date)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except Exception as ex:
            result = [0, self]

        return result

    def identify(self):
        sql = 'SELECT * FROM usuarios WHERE email = %s AND password = %s'
        
        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # Datos para la consulta
        user = (self.email, cifrado.hexdigest())

        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result