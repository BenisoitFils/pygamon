import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('manejo de grid')
#ventana.iconbitmap('')
# width es la cantidad de caracteres que ocupa la caja
#entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.DISABLED, show='*')
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER)
entrada1.grid(row=0, column=0)
# insert agrega un texto
entrada1.insert(0,'Introduce una cadena')
entrada1.insert(5, '-')
entrada1.insert(tk.END, '$')
# solo lectura
#entrada1.config(state='readonly')


# metodo pour extraire info de input
def enviar():
    print(entrada1.get())
    #pour modifier le bouton
    boton1.config(text=entrada1.get())
    #pour effacer
    #entrada1.delete(0, tk.END)
    #selectioner tout
    entrada1.select_range(0, tk.END)
    # Para hacer efectiva la selecccion del texto
    entrada1.focus()


# creamos un buton
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)


ventana.mainloop()