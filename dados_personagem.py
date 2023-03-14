import menu

nome_personagem = {1:"Nort"}
raca_personagem = {1:"Ent"}
classe_personagem ={1:"Mago"}
espec_personagem = {1:"Espaço-tempo"}
nivel_personagem = {1:1}
exp_personagem = {1:0}
next_level = {1:10}
atributos_personagem = {1:{"strenght":0,"dexterity":2,"inteligence":10,"constitution":2,"wisdown":5,"charism":1}}

def new_personagem(nome, raca, classe, especialidade):
    index = len(nome_personagem)
    index = index + 1
    nome_personagem.update({index:nome})
    raca_personagem.update({index:raca})
    classe_personagem.update({index:classe})
    espec_personagem.update({index:especialidade})
    nivel_personagem.update({index:1})
    exp_personagem.update({index:0})
    next_level.update({index:(nivel_personagem[index] * 5 + 5)})
    
def personagem_atributos(index, strenght, dexterity, inteligence, constitution, wisdown, charism):

    atributos_personagem.update({index:{'strenght':strenght,'dexterity':dexterity,'inteligence':inteligence,"constitution":constitution,'wisdown':wisdown,'charism':charism}})

    saldo = pontos_atributos(index)

    return saldo


def pontos_atributos(index):
    
    soma_pontos = atributos_personagem[index]['strenght'] + atributos_personagem[index]['dexterity'] + atributos_personagem[index]['inteligence'] + atributos_personagem[index]['constitution'] + atributos_personagem[index]['wisdown'] + atributos_personagem[index]['charism']
    
    saldo_pontos = (nivel_personagem[index] + 19) - soma_pontos 

    return saldo_pontos


def update_atributos(index,atributo,add_valor):
    valor_atual = atributos_personagem[index][atributo]
    ##print("{} + {}".format(valor_atual,add_valor))
    new_valor = valor_atual + add_valor
    ##print(new_valor)
    ##atributos_personagem.update({index:{atributo:new_valor}})
    atributos_personagem[index][atributo] = new_valor
    ##print(atributos_personagem[index])
    ##print(atributos_personagem[index][atributo])

    if(pontos_atributos(index) < 0):
        limite = True
        mensagem = "Error"
        rollback_pts = new_valor - add_valor
        atributos_personagem[index][atributo] = rollback_pts
    else:
        limite = False
        mensagem = "OK"

    return limite, mensagem
    

if(__name__ == "__main__"):
    menu.menu()