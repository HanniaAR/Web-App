"""
Proyecto Python & MySQL:
- Abrir asistente
- LogIn o registro
- Si elegimos registro, creará un usuario en la dbc
- Si elegimos, login, identificará al usuario y preguntará pssw
- Crear nota, mostrar notas, borrarlas
"""

from usuarios import actions

print("""
Acciones disponibles:
      - Register
      - Login
""")

do = actions.Actions()

action = input('What do you want to do? ')
if action == 'Register':
    do.register()
elif action == 'Login':
    do.login()
else:
    print('Invalid action')