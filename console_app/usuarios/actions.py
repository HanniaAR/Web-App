from usuarios.usuario import Usuario
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
        email = input('Write your email: ')
        password = input('Write your password: ')