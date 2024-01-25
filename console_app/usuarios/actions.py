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
        pass