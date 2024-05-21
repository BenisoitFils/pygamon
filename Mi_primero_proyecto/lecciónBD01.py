import psycopg2

conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'Ejemplo_Base'
)
print(conexion)

def insertar_ciudad(ciudad, superficie):
    cursor = conexion.cursor()
    sentencia = "INSERT INTO public.ciudad(nombre, superficie) VALUES ('"+ciudad+"', "+superficie+")"
    cursor.execute(sentencia)
    conexion.commit()

def mostrar_ciudad():
    cursor = conexion.cursor()
    sentencia = 'SELECT * FROM ciudad'
    cursor.execute(sentencia)
    registros = cursor.fetchall()
    print(registros)


def actualizar_ciudad():
    mostrar_ciudad()
    cod = int(input('Ingrese el numero de la ciudad que quiere actualizar: \n'))
    nueva_ciudad = input('Ingrese el nombre de la ciudad: \n')
    nueva_superficie = int(input('Ingrese la superficie de la '+nueva_ciudad+': \n'))
    cursor = conexion.cursor()
    sentencia = "UPDATE public.ciudad SET nombre='"+nueva_ciudad+"', superficie="+str(nueva_superficie)+" WHERE ciudad_id = "+str(cod)+""
    cursor.execute(sentencia)
    conexion.commit()
    mostrar_ciudad()


"""ciudad = input('Ingrese ciudad: \n')
superficie = input('Ingrese superficie de '+ciudad+': \n')
insertar_ciudad(ciudad,superficie)"""
actualizar_ciudad()

