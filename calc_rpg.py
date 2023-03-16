import dados_personagem
import menu

def atrib_teste(num_atrib,dificuldade,index_personagem,valor_dado):

    ##print("Atributo que será testado:\n| 1-Força\n| 2-Destreza\n| 3-Inteligência\n| 4-Constituição\n| 5-Sabedoria\n| 6-Carisma")

    if(num_atrib == 1):
        atrib = 'strenght'
    elif(num_atrib == 2):
        atrib = 'dexterity'
    elif(num_atrib == 3):
        atrib = 'inteligence'
    elif(num_atrib == 4):
        atrib = 'constitution'
    elif(num_atrib == 5):
        atrib = 'wisdown'
    elif(num_atrib == 6):
        atrib = 'charism'

    ##print(valor_dado)
    resultado_teste = valor_dado + dados_personagem.atributos_personagem[index_personagem][atrib] - dificuldade

    return resultado_teste


if(__name__ == "__main__"):
    menu.menu()