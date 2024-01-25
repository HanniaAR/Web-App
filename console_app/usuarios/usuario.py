import mysql.connector
import datetime
import hashlib

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='master_python', 
    port='3306'
)

cursor = database.cursor(buffered=True)

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
        pass