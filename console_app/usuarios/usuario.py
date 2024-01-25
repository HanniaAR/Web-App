import mysql.connector

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
        pass

    def identify(self):
        pass