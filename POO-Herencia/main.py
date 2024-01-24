import clases as c

persona = c.Person()
persona.setName('Hannia')
persona.setApellido('Arias')
persona.setAltura('1.61m')
persona.setEdad(23)

print(f'La persona es {persona.getName()} {persona.getApellido()}')
print(persona.hanblar())

ingeniero = c.Programer()
ingeniero.setName('Hrista')
ingeniero.setApellido('Martinez')
print(f'El ingeniero es {ingeniero.getName()} {ingeniero.getApellido()} y los lenguajes que domina son {ingeniero.getLenguajes()}')