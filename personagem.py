import menu

nome_personagem = {}
raca_personagem = {}
classe_personagem = {}
nivel_personagem = {}
exp_personagem = {}
atributos_personagem = {}

def ficha_personagem():

    last_personagem = len(nome_personagem)

    voltar = False

    while(not voltar):
        if(last_personagem == 0):
            print("Não existe nenhum personagem criado. Iniciando cadastro do primeiro personagem")
            new_personagem(1)
            last_personagem = len(nome_personagem)
        else:
            create_new = int(input("Deseja criar um novo personagem?\n1 - SIM\n2 - NÃO\nOpção desejada: (Somente Número) -> "))
            if(create_new == 1):
                new_index = last_personagem + 1
                print("Cadastro de Personagem {}".format(new_index))
                new_personagem(new_index)
            else:
                voltar = True
            last_personagem = len(nome_personagem)
    print("Selecione o Personagem para visualizar sua ficha:\n{}".format(nome_personagem))



def new_personagem(index):
    print("========== <> ==========")
    nome = input("Nome Personagem: ")
    raca = input("Raça: ")
    classe = input("Classe: ")

    nome_personagem.update({index:nome})
    raca_personagem.update({index:raca})
    classe_personagem.update({index:classe})

    nivel_personagem.update({index:1})
    exp_personagem.update({index:0})    

    print("====================")
    total_pts = 20
    pts_distr = 0

    while (pts_distr != total_pts):   
        print("Total de pontos para distribuir: {}".format(total_pts))
        strenght = int(input("Forca: "))
        dexterity = int(input("Destreza: "))
        inteligence = int(input("Inteligência: "))
        constitution = int(input("Constituição: "))
        wisdown = int(input("Sabedoria: "))
        charism = int(input("Carisma: "))

        pts_distr = strenght + dexterity + inteligence + constitution + wisdown + charism
        print("Você distribuiu {} pontos.".format(pts_distr))
        if(pts_distr > total_pts or pts_distr < total_pts):
            print("Corrija a distribuição de pontos.")
    
    atributos_personagem.update({index:{"strenght":strenght,"dexterity":dexterity,"inteligence":inteligence,"constitution":constitution,"wisdown":wisdown,"charism":charism}})
    ##print(atributos_personagem[index])


def new_nivel(index):
    next_level = exp_personagem[1] * 5 + 5




if(__name__ == "__main__"):
    ##menu.menu()
    ficha_personagem()