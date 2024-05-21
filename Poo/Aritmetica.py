import datetime
now = datetime.datetime.now()
print(now.strftime('%Y-%M-%D %H:%M:%S'))

print('Proporcionar 2 numero y te doy la suma restar multiplication y division')

class Aritmetica:
    def __init__(self):
        self.num1 = float(input('Ingresar primero numero\r\n'))
        self.num2 = float(input('Ingresar segundo numero\r\n'))

    def sum(self):
        return self.num1 + self.num2

    def res(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 *self.num2

    def div(self):
        return self.num1 / self.num2

aritmetica =Aritmetica()
print(f'La suma es: {aritmetica.sum()}')
print(F'La restar es: {aritmetica.res()}')
print(f'El producto es: {aritmetica.mul()}')
print(f'La division es: {aritmetica.div()}')

