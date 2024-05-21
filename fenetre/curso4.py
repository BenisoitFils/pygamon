import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('300x130')
ventana.title('login')
ventana.iconbitmap('yt.ico')
ventana.resizable(0,0)

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=3)


def vrf():
    messagebox.showinfo('Datos Login',
                        f'Usuario: {inputtxt.get()}, Password:'
                        f' {inputtxt1.get()}')


useurname1 = tk.Label(ventana, text='Username')
useurname1.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

inputtxt = tk.Entry(ventana)
inputtxt.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

password = tk.Label(ventana, text='Password')
password.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

inputtxt1 = tk.Entry(ventana, show='*')
inputtxt1.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

bt = tk.Button(ventana, text='login', command=vrf)
bt.grid(row=2, column=0, padx=5, columnspan=2)


ventana.mainloop()