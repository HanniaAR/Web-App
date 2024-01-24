# Es la posibilidad de compartir atributos / métodos entre clases

class Person:

    def getName(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellidos
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad
    
    def setName(self, name):
        self.nombre = name

    def setApellido(self, apellido):
        self.apellidos = apellido

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hanblar(self):
        return 'Estoy hablando'
    
    def caminar(self):
        return 'Estoy caminando'
    
    def dormir(self):
        return 'Estoy durmiendo'
    
class Programer(Person):

    def __init__(self) -> None:
        super().__init__()
        self.lenguajes = 'HTML, CSS, JS, PHP'
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return 'Estoy programando'
    
    def repararPC(self):
        return 'He reparado tu ordenador'