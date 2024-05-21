import tkinter as tk
import sys
from tkinter import ttk, messagebox, Menu


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400')
        self.title('App')






if __name__ =='__main__':
    app = App()
    app.mainloop()