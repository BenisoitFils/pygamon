"""un message de bienvenue a l'utilisateur
1 rentre votre mot de pass pour pouvoir acceder avec le programe
2 les option: Si quieres ver la información de lavadores presiona l, si quieres cambiar tu contraseña presiona c,
              'para modificar lavadores presiona m, para agregar presiona a, para eliminar presiona e"""



"""class Persona:
    def __init__(self,nombre=None,apellido=None):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'vous etre: {self.nombre} {self.apellido}'


class Vehiculo:
    def __init__(self,tipo,marca,modelo,color):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.color = color
"""



import _datetime
import psycopg2

now = _datetime.datetime.now()
print(now.strftime('%D %H:%M:%S'))

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    database='carwash',
    port='5432'
)


def data(v):
    info = input(v)
    return info


def mon_inf():
    cursor = conexion.cursor()
    sentencia = 'SELECT * FROM trabajadores'
    cursor.execute(sentencia)
    registro = cursor.fetchall()
    print(registro)


def mdf(id, nmb, ap):
    id_lv = int(input(id))
    nomb = input(nmb)
    apel = input(ap)
    cursor = conexion.cursor()
    sentencia = "UPDATE public.trabajadores SET nombre='" + nomb + "', apellido='" + apel + "' WHERE id_trabajadores='" + str(id_lv) + "'"
    cursor.execute(sentencia)
    conexion.commit()
    #return id_lv, nomb, apel



def ajtlvd(nj,aj):
    nnj = input(nj)
    naj = input(aj)
    cursor = conexion.cursor()
    sentencia = "INSERT INTO public.trabajadores(nombre, apellido) VALUES ('" + nnj + "', '" + naj+ "')"
    cursor.execute(sentencia)
    conexion.commit()


def elmn(idl):
    cursor = conexion.cursor()
    sentencia ="DELETE FROM trabajadores WHERE id_trabajadores= %s"
    inf = input(idl)
    valores = (inf,)
    cursor.execute(sentencia, valores)
    registros = cursor.rowcount
    print(f'eliminado {registros}')

new_pass = None
log = None
password = 'admin'
veripass = password



option = 't'
option2 = 'c'
option3 = 'm'
option4 = 'a'
option5 = 'e'

while True:
    log = data(
        'Bienvenido a su aplicación de HERCULES ingrese su contraseña para continuar por favor NB: Usted tienes 3 tentacion\n')
    if log == password:
        print('Contraseña correcta')
        break
    elif log != password:
        print('Contraseña incorrecta intente nuevamente')
        log = data('2 tentacion\n')
        if log == password:
            print('Contraseña correcta en segunda ves ')
            break
        elif log != password:
            log = data('ultima tentancion\n')
            if log == password:
                print('Contraseña correcta en la ultima ves')
                break
            else:
                print('la aplicacion esta bloquiado llama al tecnico para ayuda')







choix = data( 'Si quieres ver la información de los trabajadores presiona t, si quieres cambiar tu contraseña presiona c,'
              ' para modificar trabajadores presiona m, para agregar presiona a, para eliminar presiona e\n')
if choix == option:
    mon_inf()

elif choix == option2:
    while True:
        veripass = data('Ingrese la contraseña anterior\n')
        if veripass == password:
            new_pass = data('Introduzca su nueva contraseña\n')
            veripass = data('confirmar la contraseña\n')
            if new_pass == veripass:
                print('modificación completada exitosamente')
                break
            else:
                print('la contraseña no coincide')





elif choix == option3:
    mdf('proporcionar el nuevo id del trabajador', 'el nuevo nombre del trabajador', 'y el nuevo apellido del trabajador')
    print('el trabajador fue modificado exitosamente')
    mon_inf()



elif choix == option4:
    ajtlvd('añade el nombre del trabajador','añade el apellido del trabajador')
    print('el trabajador fue agregado exitosamente')
    mon_inf()


elif choix == option5:
    elmn('proporcionar el id a eliminar')
    mon_inf()
    conexion.close()








