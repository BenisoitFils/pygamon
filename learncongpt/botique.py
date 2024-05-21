"""l = int(input('val'))
for i in range(1,l+1):
    for j in range(1,l-i+1):
        print(" ",end="")
    for j in range(1, 2 * i - 1 + 1):
        print("* ",end="")
    print()"""

import psycopg2
import datetime

# maneja de la hora y la fechia
now = datetime.datetime.now()
fechia_hora = now.strftime("%Y-%m-%d %H:%M:%S")
fechia =  now.strftime("%Y-%m-%d")
hora = now.strftime("%H:%M:%S")



conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'AppHer'
)
print(conexion)



def diference(lun,mar,mer,jeu,ven,sam,dim):
    all_day = {'Lundi':lun,'Mardi':mar,'Mercredi':mer,'Jeudi':jeu,
               'Vendredi':ven,'Samedi':sam,'Dimanche':dim}
    meilleur = max(all_day, key=all_day.get)
    pire = min(all_day, key=all_day.get)
    print('Le meilleur jour est :',meilleur)
    print(f'Le pire jour est :{pire}')
    return all_day


# entrada de la sentencia
def entrada(vl):
    info = str(input(vl))
    return info



def insertar_producto(productos, precio, cantidad):
    cursor = conexion.cursor()
    sentencia = "INSERT INTO public.producto(productos, precio, cantidad) VALUES ('"+productos+"', "+str(precio)+", "+str(cantidad)+")"
    cursor.execute(sentencia)
    conexion.commit()



def mostrar_detalle_producto():
    cursor = conexion.cursor()
    sentencia = 'SELECT * FROM producto'
    cursor.execute(sentencia)
    registros = cursor.fetchall()
    print('             Pro    Pre   Can')
    for index, i in enumerate(registros):
        print(f'Producto {index},{i}')
    #print(registros)




def actualizar_producto():
    mostrar_detalle_producto()
    old_producto = input('Ingrese el producto  que quiere actualizar: \n')
    nuevo_producto = input('Ingrese el nuevo producto : \n')
    nuevo_precio = int(input('Ingrese el nuevo precio de(l) '+nuevo_producto+': \n'))
    nueva_cantidad = int(input('Ingrese la nueva cantidad de(l) '+nuevo_producto+': \n'))
    cursor = conexion.cursor()
    sentencia = "UPDATE public.producto SET productos='"+nuevo_producto+"', precio="+str(nuevo_precio)+", cantidad="+str(nueva_cantidad)+" WHERE productos= '"+old_producto+"'"
    cursor.execute(sentencia)
    conexion.commit()
    mostrar_detalle_producto()




def delete_producto():
    mostrar_detalle_producto()
    producto = input('engresar el producto que quiere eliminar\n')
    cursor = conexion.cursor()
    sentencia = "DELETE FROM producto WHERE productos= '"+producto+"'"
    cursor.execute(sentencia)
    conexion.commit()
    mostrar_detalle_producto()

def vendedor(cod_vendedor):
    # appelle a la fonction detail du marche
    mostrar_detalle_producto()

    producto = input('Engresar el Producto del cliente\n')
    nueva_cantidad = int(input('engresar la cantidad de(l) ' + producto + '\n'))

    cursor = conexion.cursor()
    cantidad_BD = "SELECT cantidad FROM public.producto WHERE productos= '" + producto + "'"
    cursor.execute(cantidad_BD)
    registros1 = cursor.fetchall()

    first_cantidad_BD = "SELECT cantidad_venta FROM public.vendedor WHERE id_vendedores = '"+cod_vendedor+"'"
    cursor.execute(first_cantidad_BD)
    registros3 = cursor.fetchall()

    precio_BD = "SELECT precio FROM public.producto WHERE productos= '" + producto + "'"
    cursor.execute(precio_BD)
    registros2 = cursor.fetchall()
    suma_venta = "UPDATE public.vendedor SET cantidad_venta=" + str(registros2[0][0] * nueva_cantidad + registros3[0][0]) + " WHERE id_vendedores ='"+cod_vendedor+"'"
    cursor.execute(suma_venta)

    id_BD = "SELECT id_vendedores FROM public.vendedor WHERE id_vendedores = '"+cod_vendedor+"'"
    cursor.execute(id_BD)
    registros_BD = cursor.fetchall()

    vr_id_BD = "SELECT id_vendedores FROM public.vendedor WHERE id_vendedores = '" + str(registros_BD[0][0]) + "'"
    cursor.execute(vr_id_BD)
    registros_usuario = cursor.fetchall()

    # historic de venta de todos los vendedores del mercado
    historic = "INSERT INTO public.detalle(id_vendedores,productos,precio,cantidad,fechia,hora) VALUES" \
            " ('"+str(registros_usuario[0][0])+"','"+producto+"',"+str(registros2[0][0])+","+str(nueva_cantidad)+",'"+fechia+"','"+hora+"')"
    cursor.execute(historic)
    conexion.commit()

    sentencia = "UPDATE public.producto SET cantidad= " + str(
        registros1[0][0] - nueva_cantidad) + " WHERE productos= '" + producto + "'"
    cursor.execute(sentencia)
    conexion.commit()
    mostrar_detalle_producto()


def agregar_vendedor():
    mostrar_vendedor()
    cursor = conexion.cursor()
    id_vendedor = entrada('Agregar el id de la Persona ... \n')
    nombre = entrada('Agregar el nombre  de la Persona \n')
    apellido = entrada('Agregar el apellido de ' + nombre + '\n')
    sentencia = "INSERT INTO public.vendedor(id_vendedores, nombre, apellido, cantidad_venta) VALUES ('" + id_vendedor + "', '" + str(nombre) + "', '" + str(apellido) + "','0')"
    cursor.execute(sentencia)
    conexion.commit()



def mostrar_vendedor():
    cursor = conexion.cursor()
    sentencia = 'SELECT * FROM vendedor'
    cursor.execute(sentencia)
    registros = cursor.fetchall()
    print('                Id          Nom       Ape       can')
    for index, i in enumerate(registros):
        print(f'Persona {index},{i}')



def historic():
   cursor = conexion.cursor()
   sentencia = "SELECT * FROM detalle"
   cursor.execute(sentencia)
   registro_historic = cursor.fetchall()
   for index, i in enumerate(registro_historic):
       print(f'Venta {index},{i}')



def delete_vendedor():
    mostrar_vendedor()
    vendedor = input('engresar el id_vendedor que quiere eliminar\n')
    cursor = conexion.cursor()
    sentencia = "DELETE FROM vendedor WHERE id_vendedores= '" + vendedor + "'"
    cursor.execute(sentencia)
    conexion.commit()
    mostrar_vendedor()



menu = int(input('Bienvenido a AppHer para agregar productos engresar 1,para verificar 2,para modificar 3 '
                 'para eliminar 4, para vendedor 5, para agregar ventidor 6, para verificar vendedores 7 para ver historic de venta 8\n'))




if menu == 1:
    productos = entrada('Agregar el nombre del producto ... \n')
    precio = entrada('Agregar el precio  de(l) '+productos+'\n')
    cantidad = entrada('Agregar la cantidad  de(l) ' +productos+ '\n')
    insertar_producto(productos, precio, cantidad)
    mostrar_detalle_producto()




if menu == 2:
    mostrar_detalle_producto()



if menu == 3:
    actualizar_producto()



if menu == 4:
    delete_producto()



if menu == 5:
    usuario = input('Ingresar tu usuario para continuar')
    cursor = conexion.cursor()
    id_BD = "SELECT id_vendedores FROM public.vendedor WHERE id_vendedores = '" + str(usuario) + "'"
    cursor.execute(id_BD)
    registros_BD = cursor.fetchall()

    usuario_verification = input('verificar tu usuario para continuar')
    if usuario_verification == str(registros_BD[0][0]):
        vendedor(str(registros_BD[0][0]))
    else:
        print('usuario no exsiste')




if menu == 6:
    agregar_vendedor()
    mostrar_vendedor()



if menu == 7:
    mostrar_vendedor()



if menu == 8:
    historic()



if menu == 9:
   delete_vendedor()
