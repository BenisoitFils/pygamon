class Persona:
    def __init__(self):
        self.nombre = 'Juan'
        self.apellido = 'perez'
        self.edad = 28

Persona1 = Persona()
print(Persona1.nombre)
print(Persona1.apellido)
print(Persona1.edad)

class Personass:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

Personass1 = Personass('juan ','perez ',28)
print(Personass1.nombre)
print(Personass1.apellido)
print(Personass1.edad)

personass2 = Personass('Karla ','Pierre ',25)
print(f'persona1 {personass2.nombre}{personass2.apellido}{personass2.edad}')

personass2.nombre = 'Darla '
personass2.apellido = 'uselie '
personass2.edad = 26

print(f'persona1 {personass2.nombre}{personass2.apellido}{personass2.edad}')

class Personas:
    def __init__(self):
        self.nombre = input('ingresar el nombre\r\n')
        self.apellido = input('ingresar apellida\r\n')
        self.edad = input('ingresar edad\r\n')

Personas1 = Personas()
print(f'Nombre: {Personas1.nombre}')
print(f'Apellido: {Personas1.apellido}')
print(f'Edad: {Personas1.edad}')