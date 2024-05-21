playlist = {} #diccionario vasio
playlist ['canciones'] = [] # lista vacia de canciones
  # foncion principal
def app():

    # agregar playlist
     agregar_playlist = True
     while agregar_playlist:
         nombre_playlist = input('como desea nombrar la playlist? \r\n')
         if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            # ya tenemos un nombre,desactivar el true
            agregar_playlist = False
            # mandar llamar la foncion para agregar canciones
            agregar_canciones()
            print(playlist)
def agregar_canciones():
    # bandera para agregar canciones
    agregar_cancion = True
    while agregar_cancion:
        # preguntar al usuario que cancion desean agregar
         nombre_playlist = playlist['nombre']
         pregunta = f'\r\n agregar canciones para la playlist' \
                    f'{nombre_playlist}:\r\n'
         pregunta += 'escribe "x" para dejar de agregar canciones \r\n'
         cancion = input(pregunta)
         if cancion == 'X':
             # dejar de agregar cancion
            agregar_cancion = False
             # mostrar resumen de la playlist
            mostrar_resumen()
         else:
             # agregar las canciones a la playlist
             playlist['canciones'].append(cancion)
def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'playlist: {nombre_playlist} \r\n')
    print('canciones: \r\n')
    for cancion in playlist ['canciones']:
        print(cancion)
app()
