import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('manejo de grid')

#Definimos una variable que podremos modificar posteriormente (set), leer (get)
entrada_var1 = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)
# insert agrega un texto
#entrada1.insert(0,'Introduce una cadena')
#entrada1.insert(5, '-')
#entrada1.insert(tk.END, '$')


# metodo pour extraire info de input
def enviar():
    # Recuperamos la modificacion a partir de la variable sociada con la caja de texto
    boton1.config(text=entrada_var1.get())
    # Modification utilizamos lavariable de texto y el metodo set
    entrada_var1.set('Cambio...')
    # Recuperamos la information
    print(entrada_var1.get())
    print(entrada1.get())


# creamos un buton
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)


ventana.mainloop()