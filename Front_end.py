from tkinter import *
from tkinter import ttk

def verificaratrib ():
    Fo=int(NPForca.get())
    De=int(NPDestreza.get())
    In=int(+NPInteligencia.get())
    Co=int(NPConstituicao.get())
    Sa=int(NPSab.get())
    Ca=int(NPCarisma.get())
    Total= Fo + De + In + Co + Sa + Ca
    print(Total)
app = Tk()
app.title("RpgBoard")
app.geometry("800x600")

nb = ttk.Notebook(app)
nb.place(x=0,y=0,width =800,height=600)

lp = Frame(nb)
nb.add(lp,text="Lista de Personagens")

cp = Frame(nb)
nb.add(cp,text="Criar Personagem")


Pessoal = Frame(cp, background= "#fff")
Pessoal.place(x=5,y=30,width=450,height=130)
Label(Pessoal,text="1. Pessoal",background="#fff",).place(x=30,y=10,width =100,height=20,anchor= CENTER)

#nome
NPN= Label(Pessoal, text="Nome")
NPN.place(x=5,y=40,width =100,height=20)

NPNome = Entry(Pessoal)
NPNome.place(x=115,y=40,width =300,height=20)


##raça
NPR= Label(Pessoal, text="Raça")
NPR.place(x=5,y=70,width =100,height=20)

NPRaca = Entry(Pessoal)
NPRaca.place(x=115,y=70,width =300,height=20)


#classe
NPC= Label(Pessoal, text="Classe")
NPC.place(x=5,y=100,width =100,height=20)

NPClasse = Entry(Pessoal)
NPClasse.place(x=115,y=100,width =300,height=20)



#atributos
atributos = Frame(cp, background= "#fff")
atributos.place(x=460,y=30,width=330,height=220)
Label(atributos,text="2. Atributos",background="#fff",).place(x=35,y=10,width =100,height=20,anchor= CENTER)
#forca
NPFor= Label(atributos, text="Força")
NPFor.place(x=5,y=40,width =100,height=20)

NPForca = Entry(atributos)
NPForca.place(x=115,y=40,width =50,height=20)

#destreza
NPDex= Label(atributos, text="Destreza")
NPDex.place(x=5,y=70,width =100,height=20)

NPDestreza = Entry(atributos)
NPDestreza.place(x=115,y=70,width =50,height=20)

#inteligencia
NPInt= Label(atributos, text="Inteligencia")
NPInt.place(x=5,y=100,width =100,height=20)

NPInteligencia = Entry(atributos)
NPInteligencia.place(x=115,y=100,width =50,height=20)

#Constituiçao
NPConst= Label(atributos, text="Constituição")
NPConst.place(x=5,y=130,width =100,height=20)

NPConstituicao = Entry(atributos)
NPConstituicao.place(x=115,y=130,width =50,height=20)

#Sabedoria
NPWis= Label(atributos, text="Constituição")
NPWis.place(x=5,y=160,width =100,height=20)

NPSab = Entry(atributos)
NPSab.place(x=115,y=160,width =50,height=20)

#Carisma
NPChar= Label(atributos, text="Constituição")
NPChar.place(x=5,y=190,width =100,height=20)

NPCarisma = Entry(atributos)
NPCarisma.place(x=115,y=190,width =50,height=20)

btn1= Button (atributos,text= "Verificar",command=verificaratrib).place(x=150,y=10,width =100,height=20)


le = Frame(nb)
nb.add(le,text="Lista de Equpipamentos")

ce = Frame(nb)
nb.add(le,text="cadastrar Equpipamentos")

dado = Frame(nb)
nb.add(dado,text="Girar dado")














app.mainloop()