from tkinter import *
root = Tk()
root.title('Prueba')
root.geometry('300x700')
root.minsize(250,500)
root.maxsize(300,750)

def Take_input():

    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if (INPUT == 'verdadero'):
        Output.insert(END, 'Respuesta correcta usted sabe mucho buena suerte')
    else:
        Output.insert(END, "Mala respuesta debe buscar mas conocimiento.")

def Take_input1():
    INPUT1 = inputtxt1.get('1.0', 'end-1c')
    print(INPUT1)
    if (INPUT1 == 'verdadero'):
        Output1.insert(END, 'Respuesta correcta usted sabe mucho buena suerte')
    else:
        Output1.insert(END, "Mala respuesta debe buscar mas conocimiento.")

def Take_input2():
    INPUT2 = inputtxt2.get('1.0', 'end-1c')
    print(INPUT2)
    if (INPUT2 == 'verdadero'):
        Output2.insert(END, 'Respuesta correcta usted sabe mucho buena suerte')
    else:
        Output2.insert(END, "Mala respuesta debe buscar mas conocimiento.")

def Take_input3():
    INPUT3 = inputtxt3.get('1.0', 'end-1c')
    print(INPUT3)
    if (INPUT3 == 'falso'):
        Output3.insert(END, 'Respuesta correcta usted sabe mucho buena suerte')
    else:
        Output3.insert(END, "Mala respuesta debe buscar mas conocimiento.")

l = Label(root,text='Responde verdadero o falso \r\n Android es la sistema explotacíon de GOOGLE')
inputtxt = Text(root,width=25,height=1,bg='light gray')

Output = Text(root, height=2,
              width=25,
              bg="light cyan")

#Display = Button(root, height=1,width=20,text="Mostrar",command=Take_input)

l.pack()
inputtxt.pack()
Output.pack()
#Display.pack()



l1 = Label(root,text='El área de Chile es 756.626 km2')
inputtxt1 = Text(root,width=25,height=1,bg='light gray')
Output1 = Text(root,width=25,height=2,bg='light cyan')
#Display1 = Button(root,text='Mostrar',width=20,height=1,command=Take_input1)

l1.pack()
inputtxt1.pack()
Output1.pack()
#Display1.pack()

l2 = Label(root,text='Paulina es la mujer mas bonita del mundo')
inputtxt2 = Text(root,width=25,height=1,bg='light gray')
Output2 = Text(root,width=25,height=2,bg='light cyan')
#Display2 = Button(root,text='Mostrar',width=20,height=1,command=Take_input2)

l2.pack()
inputtxt2.pack()
Output2.pack()
#Display2.pack()

l3 = Label(root,text='Las agujas del reloj siempre va de derecha a izquierda')
inputtxt3 = Text(root,width=25,height=1,bg='light gray')
Output3 = Text(root,width=25,height=2,bg='light cyan')
Display3 = Button(root,text='Mostrar',width=20,height=1,command=Take_input3)

l3.pack()
inputtxt3.pack()
Output3.pack()
Display3.pack()

root.mainloop()