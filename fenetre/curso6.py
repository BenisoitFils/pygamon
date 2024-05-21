import tkinter as tk
# dans tkinter importe themes tkinter,epuis boite message
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

ventana = tk.Tk()
ventana.geometry('600x400+400+200')
ventana.title('Componentes')

def crear_componentes_tabulador1(tabulador):
    # Agregamos una etiqueta y un componente de entrada
    etiqueta1 = ttk.Label(tabulador, text='Nombre:')
    etiqueta1.grid(row=0, column=0, sticky=tk.E)
    entrada1 = ttk.Entry(tabulador, width=30)
    entrada1.grid(row=0, column=1, padx=5, pady=5)

    # Agregamos un boton
    def enviar():
        messagebox.showinfo('Mensaje', f'Nombre: {entrada1.get()}')

    boton1 = ttk.Button(tabulador, text='Enviar', command=enviar)
    boton1.grid(row=1, column=0, columnspan=2)

def crear_componentes_tabulador2(tabulador):
    contenido = 'Este es mi texto con el contenido'
    # Creamos el componente de scroll
    # el wrap=tk.WORD es para no cortar las palabras
    scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD)
    scroll.insert(tk.INSERT, contenido)
    # Mostramos el componente
    scroll.grid(row=0, column=0)

def crear_componentes_tabulador3(tabulador):
    # Creamos una lista usando data list comprehension
    datos = [x+1 for x in range(10)]
    combobox = ttk.Combobox(tabulador, width=15, values=datos)
    combobox.grid(row=0, column=0, padx=10, pady=10)
    # Seleccionamos un elemento por default a mostrar
    combobox.current(5)
    # Agregar un boton para saber que opcion selecciono el usuario
    def mostrar_valor():
        messagebox.showinfo('Valor seleccionado', f'Valor seleccionado: {combobox.get()}')

    boton1 = ttk.Button(tabulador, text='Mostrar Valor Seleccionado', command=mostrar_valor)
    boton1.grid(row=0, column=1)

def crear_componentes_tabulador4(tabulador):
    imagen = tk.PhotoImage(file='pau.png')
    def mostrar_titulo():
        messagebox.showinfo('Mas Info imagen', f'Nombre imagen: {imagen.cget("file")}')
    boton_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)
    boton_imagen.grid(row=0, column=0)

def crear_componentes_tabulador5(tabulador):
    # Creamos el componente de barra progreso
    barra_progreso = ttk.Progressbar(tabulador, orient='horizontal', length=550)
    barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
    def ejecutar_barra():
        barra_progreso['maximum'] = 100
        for valor in range(101):
            # Mandamos a esperar un poco antes de continuar con la ejecucion de barra
            sleep(0.05)
            # Incrementamos nuestra barra de progreso
            barra_progreso['value'] = valor
            # Actualizamos la barra de progreso
            barra_progreso.update()
        barra_progreso['value'] = 0

    def ejecutar_ciclo():
        barra_progreso.start()

    def detener():
        barra_progreso.stop()

    def detener_despues():
        esperar_ms = 1000
        ventana.after(esperar_ms, barra_progreso.stop())

    # Botones para controlar los eventos de una barra de progreso
    boton_inicio = ttk.Button(tabulador, text='Ejecutar Barra de Progreso', command=ejecutar_barra)
    boton_inicio.grid(row=1,column=0)

    boton_ciclo = ttk.Button(tabulador, text='Ejecutar ciclo', command=ejecutar_ciclo)
    boton_ciclo.grid(row=1, column=1)

    boton_detener = ttk.Button(tabulador, text='Detener Ejecucion', command=detener)
    boton_detener.grid(row=1, column=2)
    boton_despues = ttk.Button(tabulador, text='Detener Ejecucion despues', command=detener_despues)
    boton_despues.grid(row=1, column=3)
def crear_tabs():
    # ceamos un tab control,para ello usamos la clase Notebook
    control_tabulador = ttk.Notebook(ventana)
    # Agregamos un marco (frame) para agregar dentro del tab y organizar elementos
    tabulador1 = ttk.Frame(control_tabulador)
    # Agregamos el tabulador al control de tabuladores
    control_tabulador.add(tabulador1, text='Tabulador1')
    # Mostrar el tabulador
    control_tabulador.pack(fill='both')
    #Creamos los componentes del tabulador1
    crear_componentes_tabulador1(tabulador1)
    # Creamos un segundo tabulador
    tabulador2 = ttk.LabelFrame(control_tabulador, text= 'Contenido')
    control_tabulador.add(tabulador2, text='Tabulador 2')
    # Creamos los componentes del segundo tabulador
    crear_componentes_tabulador2(tabulador2)
    # Crear un tercer tabulador
    tabulador3 = ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador3, text='Tabulador 3')
    # Creamos los componentes del tercer tabulador
    crear_componentes_tabulador3(tabulador3)
    # Crear el cuarto tabulador
    tabulador4 = ttk.LabelFrame(control_tabulador, text='imagen')
    control_tabulador.add(tabulador4, text='Tabulador 4')
    # Creamos los componentes del cuarto tabulador
    crear_componentes_tabulador4(tabulador4)
    # Creamos un quinto tabulador
    tabulador5 = ttk.LabelFrame(control_tabulador, text='Progress Bar')
    control_tabulador.add(tabulador5, text='tabulador 5')
    # Creamos los componentes del quinto tabulador
    crear_componentes_tabulador5(tabulador5)



crear_tabs()

ventana.mainloop()