from tkinter import *
from tkinter import ttk
PI=20
Fo=0
De=0
In=0
Co=0
Sa=0
Ca=0
def verificaEqui():
    NEq= Label(Equi, text="Nenhum equipamento registrado")
    NEq.place(x=170,y=45,width = 275,height=20)







def verificaratrib ():
    Fo=int(NPForca.get())
    De=int(NPDestreza.get())
    In=int(NPInteligencia.get())
    Co=int(NPConstituicao.get())
    Sa=int(NPSab.get())
    Ca=int(NPCarisma.get())
    Total= int(Fo + De + In + Co + Sa + Ca)
    Pr=PI - Total
    PR= Label(atributos, text="Pontos Restantes %i" %Pr)
    PR.place(x=5,y=17,width =150,height=17)
    if(Total == PI):
        Salvar = Frame(atributos, background= "#fff")
        Salvar.place(x=200,y=30,width=100,height=20)
        btn1= Button (Salvar,text= "salvar",command=verificaratrib).place(x=0,y=0,width =100,height=20)
        
    else:
        Salvar = Frame(atributos, background= "#fff")
        Salvar.place(x=200,y=30,width=100,height=20)


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
NPForca.insert(0, "0")

#destreza
NPDex= Label(atributos, text="Destreza")
NPDex.place(x=5,y=70,width =100,height=20)

NPDestreza = Entry(atributos)
NPDestreza.place(x=115,y=70,width =50,height=20)
NPDestreza.insert(0, "0")

#inteligencia
NPInt= Label(atributos, text="Inteligencia")
NPInt.place(x=5,y=100,width =100,height=20)

NPInteligencia = Entry(atributos)
NPInteligencia.place(x=115,y=100,width =50,height=20)
NPInteligencia.insert(0, "0")

#Constituiçao
NPConst= Label(atributos, text="Constituição")
NPConst.place(x=5,y=130,width =100,height=20)

NPConstituicao = Entry(atributos)
NPConstituicao.place(x=115,y=130,width =50,height=20)
NPConstituicao.insert(0, "0")
#Sabedoria
NPWis= Label(atributos, text="Constituição")
NPWis.place(x=5,y=160,width =100,height=20)

NPSab = Entry(atributos)
NPSab.place(x=115,y=160,width =50,height=20)
NPSab.insert(0, "0")
#Carisma
NPChar= Label(atributos, text="Constituição")
NPChar.place(x=5,y=190,width =100,height=20)

NPCarisma = Entry(atributos)
NPCarisma.place(x=115,y=190,width =50,height=20)
NPCarisma.insert(0, "0")

btn1= Button (atributos,text= "Verificar",command=verificaratrib).place(x=200,y=5,width =100,height=20)
PR= Label(atributos, text="Pontos Restantes 20" )
PR.place(x=5,y=17,width =150,height=17)




#equipamentos
Equi = Frame(cp, background= "#fff")
Equi.place(x=5,y=165,width=450,height=145)
Label(Equi,text="3. Equipamentos",background="#fff",).place(x=55,y=10,width =100,height=20,anchor= CENTER)

Equipamentos= Label(Equi, text="Insira o Id do equipamento e clique em verificar")
Equipamentos.place(x=5,y=20,width = 440,height=20)

#equi1
Equi1= Label(Equi, text="1")
Equi1.place(x=5,y=45,width = 20,height=20)

IDequi1 = Entry(Equi)
IDequi1.place(x=35,y=45,width =40,height=20)
IDequi1.insert(0, "0")
eq1= int(IDequi1.get())
VID1= Button (Equi,text= "Verificar",command=verificaEqui).place(x=85,y=45,width =80,height=20)


#equi2
Equi2= Label(Equi, text="1")
Equi2.place(x=5,y=70,width = 20,height=20)

IDequi2 = Entry(Equi)
IDequi2.place(x=35,y=70,width =40,height=20)
IDequi2.insert(0, "0")
VID2= Button (Equi,text= "Verificar",command=verificaratrib).place(x=85,y=70,width =80,height=20)

#equi3
Equi3= Label(Equi, text="1")
Equi3.place(x=5,y=95,width = 20,height=20)

IDequi3 = Entry(Equi)
IDequi3.place(x=35,y=95,width =40,height=20)
IDequi3.insert(0, "0")
VID3= Button (Equi,text= "Verificar",command=verificaratrib).place(x=85,y=95,width =80,height=20)

#equi4
Equi4= Label(Equi, text="1")
Equi4.place(x=5,y=120,width = 20,height=20)

IDequi4 = Entry(Equi)
IDequi4.place(x=35,y=120,width =40,height=20)
IDequi4.insert(0, "0")
VID4= Button (Equi,text= "Verificar",command=verificaratrib).place(x=85,y=120,width =80,height=20)


#Skill
Skill = Frame(cp, background= "#fff")
Skill.place(x=5,y=315,width=450,height=145)
Label(Skill,text="4. Skill",background="#fff",).place(x=55,y=10,width =100,height=20,anchor= CENTER)

skills= Label(Skill, text="Insira o Id da e clique em verificar")
skills.place(x=5,y=20,width = 440,height=20)

#skill1
skill1= Label(Skill, text="1")
skill1.place(x=5,y=45,width = 20,height=20)

IDskill1 = Entry(Skill)
IDskill1.place(x=35,y=45,width =40,height=20)
IDskill1.insert(0, "0")
VIDS1= Button (Skill,text= "Verificar",command=verificaratrib).place(x=85,y=45,width =80,height=20)

#skill2
skill2= Label(Skill, text="1")
skill2.place(x=5,y=70,width = 20,height=20)

IDskill2 = Entry(Skill)
IDskill2.place(x=35,y=70,width =40,height=20)
IDskill2.insert(0, "0")
VIDS2= Button (Skill,text= "Verificar",command=verificaratrib).place(x=85,y=70,width =80,height=20)

#skill3
skill3= Label(Skill, text="1")
skill3.place(x=5,y=95,width = 20,height=20)

IDskill3 = Entry(Skill)
IDskill3.place(x=35,y=95,width =40,height=20)
IDskill3.insert(0, "0")
VIDS3= Button (Skill,text= "Verificar",command=verificaratrib).place(x=85,y=95,width =80,height=20)

#skill4
skill4= Label(Skill, text="1")
skill4.place(x=5,y=120,width = 20,height=20)

IDskill4 = Entry(Skill)
IDskill4.place(x=35,y=120,width =40,height=20)
IDskill4.insert(0, "0")
VIDS4= Button (Skill,text= "Verificar",command=verificaratrib).place(x=85,y=120,width =80,height=20)


le = Frame(nb)
nb.add(le,text="Lista de Equpipamentos")

ce = Frame(nb)
nb.add(le,text="cadastrar Equpipamentos")

dado = Frame(nb)
nb.add(dado,text="Girar dado")

teste= Label(app, text="%s" %NPForca.get())
teste.place(x=5,y=500,width =100,height=20)














app.mainloop()