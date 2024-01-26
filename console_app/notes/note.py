import usuarios.connection as conn

connect = conn.connect()
database = connect[0]
cursor = connect[1]

class Note:

    def __init__(self, user_id, title, desc) -> None:
        self.user = user_id
        self.title = title
        self.desc = desc

    def save(self):
        sql = 'INSERT INTO notas VALUES (null, %s, %s, %s, NOW())'
        nota = (self.user, self.title, self.desc)

        cursor.execute(sql, nota)
        database.commit()

        return [cursor.rowcount, self]