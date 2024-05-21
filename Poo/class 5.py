class Persona:
    def __init__(self,nombre,apellido,edad,*args,**terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.terminos = terminos

    def mostral_detalle(self):
        print(f'Nombre: {self.nombre},Apellido: {self.apellido},Edad: {self.edad} ,{self.args} ,{self.terminos}')

persona = Persona('Juan ','Perez ',28 ,'4434',1,2,3,4, ONU='Organisation Nation Unis')

# dos maneras para llama la function
#persona.mostral_detalle()
#Persona.mostral_detalle(persona)
#print(persona.phone)
#    print(persona.phone)
#AttributeError: 'Persona' object has no attribute 'phone'

Persona.mostral_detalle(persona)

persona1 = Persona('Paulina ','Charite ','29')
persona1.mostral_detalle()
persona1.phone = +5095551566
print(persona1.phone)
