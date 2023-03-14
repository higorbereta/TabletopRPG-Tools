import menu

nome_personagem = {} ##{1:"Kirito",2:"Higor"}
raca_personagem = {} ##{1:"Elfo"}
classe_personagem = {} ##{1:"Mago"}
nivel_personagem = {} ##{1:1}
exp_personagem = {} ##{1:0}
atributos_personagem = {} ##{1:{"strenght":0,"dexterity":2,"inteligence":10,"constitution":2,"wisdown":5,"charism":1}}

def new_personagem(nome, raca, classe):
    index = len(nome_personagem)
    index = index + 1
    nome_personagem.update({index:nome})
    raca_personagem.update({index:raca})
    classe_personagem.update({index:classe})
    nivel_personagem.update({index:1})
    exp_personagem.update({index:0})
    
def personagem_atributos(index, strenght, dexterity, inteligence, constitution, wisdown, charism):

    atributos_personagem.update({index:{"strenght":strenght,"dexterity":dexterity,"inteligence":inteligence,"constitution":constitution,"wisdown":wisdown,"charism":charism}})

    soma_pontos = atributos_personagem[index]['strenght'] + atributos_personagem[index]['dexterity'] + atributos_personagem[index]['inteligence'] + atributos_personagem[index]['constitution'] + atributos_personagem[index]['wisdown'] + atributos_personagem[index]['charism']

    saldo_pontos = (nivel_personagem[index] + 19) - soma_pontos

    return saldo_pontos

if(__name__ == "__main__"):
    menu.menu()