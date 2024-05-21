import tkinter as tk
from tkinter import ttk, messagebox

class LoginVentana(tk.Tk):
    def __init__(self):
        super(LoginVentana, self).__init__()

        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('yt.ico')
        self.resizable(0,0)

        #configuracion del grid

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        # Creamos los componentes
        self._crear_componentes()

    # Definir el metodo crear_componentes
    def _crear_componentes(self):

        # Usuario
        usuario_etiqueta = tk.Label(self, text='Username')
        usuario_etiqueta .grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.usuario_entrada = tk.Entry(self)
        self.usuario_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        # password
        password_etiqueta = tk.Label(self, text='Password')
        password_etiqueta.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.password_entrada = tk.Entry(self, show='*')
        self.password_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        # boton login
        bt = ttk.Button(self, text='login', command=self._login)
        bt.grid(row=2, column=0, padx=5, columnspan=2)


    def _login(self):
        messagebox.showinfo('Datos Login',
                            f'Usuario: {self.usuario_entrada.get()}, Password:'
                            f' {self.password_entrada.get()}')

if __name__== '__main__':
    login_ventana = LoginVentana()
    login_ventana.mainloop()