from tkinter import *
import os
#command inscription
def Incription_code():
    nom_Inscription = NomInscription_entry.get()
    pass_Inscription = PassInscription_entry.get()
    File_inscription_name = os.listdir()
    if str(nom_Inscription) + '.txt' in File_inscription_name:
        print('Erreur 3 : le nom ')
    else:
        File = open(str(nom_Inscription)+'.txt','w')
        File.write(str(nom_Inscription)+':'+str(pass_Inscription))
        File.close()
        print('votre compte a ete cree avec succes')
#command login
def Login_code():
    nom_Login = Nomlogin_entry.get()
    pass_Login = Passlogin_entry.get()
    File_login_name = os.listdir()
    if str(nom_Login)+'.txt'in File_login_name:
        File1 = open(str(nom_Login)+'.txt', 'r')
        liste_info_login = File1.read().split(':')
        File1.close()
        if pass_Login == liste_info_login[1]:
            print('message 1 : Bienvenue')
        else:
            print('erreur 2 le mot de pass est faux')
    else:
        print('Erreur 1 : identifient existe pas')


def Login_Window_open() :
    Login_Window = Tk()
    Login_Window.title('Login:')
    Login_Window.geometry('470x400')
    Login_Window.minsize(470,400)
    Login_Window.maxsize(470,400)
    Login_Window.config(bg='#282882')
    Login_frame = Frame(Login_Window,bg='#6D6DE3')

    Nom = Label(Login_frame,text='Nom:',font=('Arial',20),width=15,height=1,bg='#6D6DE3',fg='black')
    Nom.grid(row=0,column=0)
    global Nomlogin_entry
    Nomlogin_entry = Entry(Login_frame,font=('Arial',18),bg='white',fg='black',width=25)
    Nomlogin_entry.grid(row=0,column=1)

    Pass = Label(Login_frame, text='Mot de pass:', font=('Arial', 20), width=15, height=1, bg='#6D6DE3', fg='black')
    Pass.grid(row=2, column=0)
    global Passlogin_entry
    Passlogin_entry = Entry(Login_frame, font=('Arial', 18), bg='white', fg='black', width=25,show='*')
    Passlogin_entry.grid(row=2, column=1)

    #Space
    Space = Label(Login_frame,text='',bg='#6D6DE3',height=1)
    Space.grid(row=4,column=0)

    # button login
    Login_button = Button(Login_frame, text='Login', font=('Arial', 18), bg='white', fg='black',command=Login_code)
    Login_button.grid(row=4, column=1)

    Login_frame.pack(expand=YES)
    Login_Window.mainloop()

def Inscription_Window_open() :
    Inscription_Window = Tk()
    Inscription_Window.title('Inscription:')
    Inscription_Window.geometry('470x400')
    Inscription_Window.minsize(470,400)
    Inscription_Window.maxsize(470,400)
    Inscription_Window.config(bg='#282882')
    Inscription_frame = Frame(Inscription_Window,bg='#6D6DE3')

    Nom = Label(Inscription_frame,text='Nom:',font=('Arial',20),width=15,height=1,bg='#6D6DE3',fg='black')
    Nom.grid(row=0,column=0)
    global NomInscription_entry
    NomInscription_entry = Entry(Inscription_frame,font=('Arial',18),bg='white',fg='black',width=25)
    NomInscription_entry.grid(row=0,column=1)

    Pass = Label(Inscription_frame, text='Mot de pass:', font=('Arial', 20), width=15, height=1, bg='#6D6DE3', fg='black')
    Pass.grid(row=2, column=0)
    global PassInscription_entry
    PassInscription_entry = Entry(Inscription_frame, font=('Arial', 18), bg='white', fg='black', width=25,show='*')
    PassInscription_entry.grid(row=2, column=1)

    #Space
    Space = Label(Inscription_frame,text='',bg='#6D6DE3',height=1)
    Space.grid(row=4,column=0)

    # button login
    Inscription_button = Button(Inscription_frame, text='Inscription', font=('Arial', 18), bg='white', fg='black',command=Incription_code)
    Inscription_button.grid(row=4, column=1)

    Inscription_frame.pack(expand=YES)
    Inscription_Window.mainloop()

menu_window = Tk()
menu_window.title("menu:")
menu_window.geometry("350x175")
menu_window.minsize(350,175)
menu_window.maxsize(350,175)
menu_window.config(bg="#007082")
menu_frame = Frame(menu_window,width=310,height=135,bg="black")

#creation du bouton login:
login_bouton = Button(menu_frame,text="login",font=("Arial",20), bg="white",fg="black",width=8, height=3,command=Login_Window_open)
login_bouton.grid(row=0,column=0)

#creation du bouton inscription
inscription_bouton = Button(menu_frame,text="inscription",font=("Arial",20), bg="white",fg="black",width=8, height=3,command=Inscription_Window_open)
inscription_bouton.grid(row=0,column=1)

menu_frame.pack(expand=YES)
menu_window.mainloop()