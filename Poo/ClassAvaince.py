"""class Persona:
    contador_personas = 0

    def __init__(self,nombre,edad):
        Persona.contador_personas += 1
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return F'Persona [{self.id_persona} {self.nombre} {self.edad}]'

persona1 = Persona('Juan ',28)
print(persona1)
persona2 = Persona('Karla ',23)
print(persona2)
persona3 = Persona('Hercules ',30)
print(persona3)
print(F'Valor contador persona: {Persona.contador_personas}')"""

class Persona:
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self,nombre,edad):
#        Persona.contador_personas += 1
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return F'Persona [{self.id_persona} {self.nombre} {self.edad}]'

persona1 = Persona('Juan ',28)
print(persona1)
persona2 = Persona('Karla ',23)
print(persona2)
persona3 = Persona('Hercules ',30)
print(persona3)
# a chaque fois on appelle la fonction entonces uno mas:
Persona.generar_siguiente_valor()
persona4 = Persona('Maria ',27)
print(persona4)
print(F'Valor contador persona: {Persona.contador_personas}')