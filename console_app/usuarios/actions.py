from usuarios.usuario import Usuario
from notes.actions import Actions as NoteActions
class Actions:
    
    def register(self):
        print('\nLet`s start with your register...')
        name = input('Write your name: ')
        last_name = input('Write your last name: ')
        email = input('Write your email: ')
        password = input('Write your password: ')

        usuario = Usuario(name, last_name, email, password)
        add = usuario.register()

        if add[0] >= 1:
            print(f'Se ha registrado {add[1].name} con el email {add[1].email}')
        else:
            print('No se ha registrado correctamente')
    
    def login(self):
        print('\nWrite your credentianls')
        try:
            email = input('Write your email: ')
            password = input('Write your password: ')

            usuario = Usuario('', '', email, password)
            login = usuario.identify()

            if email == login[3]:
                print(f'Welcome {login[1]}, login succesfully')
                self.nextActions(login)

        except Exception as ex:
            #print(type(ex))
            #print(type(ex).__name__)
            print('Login incorrecto')
        
    def nextActions(self, usuario):
        print("""
        Acciones disponibles:
              - Crear Nota [C]
              - Mostrar tus notas [M]
              - Eliminar Nota [D]
              - Salir [S]
        """)

        do = NoteActions()

        action = (input('What do you want?: ')).upper()

        if action == 'C':
            do.create(usuario)
            self.nextActions(usuario)
        elif action == 'M':
            print('Mostrando Nota(s)...')
            self.nextActions(usuario)
        elif action == 'D':
            print('Borrando Nota...')
            self.nextActions(usuario)
        elif action == 'S':
            print('Closing...')
            exit()