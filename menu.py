
import dados_personagem

def menu():

    print("Bem vindo ao Tabletop RPG Tool")

    encerrar = False

    while(not encerrar):

        print(" 1 - Ficha de Personagem\n 2 - Dado \n 0 - Encerrar")
        menu_option = int(input("Selecione a opção desejada -> "))
        if(menu_option == 1):
            ficha_personagem()
        if(menu_option == 2):
            print("Dado")
        if(menu_option == 0):
            print("Encerrando aplicação")
            encerrar = True
            
def ficha_personagem():
    last_personagem = len(dados_personagem.nome_personagem)
    voltar = False

    while(not voltar):
        if(last_personagem == 0):
            print("Nâo existe nenhum personagem criado.")
            print("Iniciando cadastro do primeiro personagem.")
            create_personagem()
            last_personagem = len(dados_personagem.nome_personagem)
            atributos_personagem(last_personagem)
        else:
            print("Lista de Personagens:\n", dados_personagem.nome_personagem)
            create_new = int(input("Deseja criar um novo personagem ou Acessar uma ficha?\n| 1-Criar novo Personagem\n| 2-Acessar uma ficha\n| 3-Voltar\n"))
            if(create_new == 1):
                print("Iniciando criação novo personagem.")
                create_personagem()
                last_personagem = len(dados_personagem.nome_personagem)
                atributos_personagem(last_personagem)
                print("Personagem {} criado.".format(last_personagem))
            elif(create_new == 2):
                num_personagem = int(input("Número do personagem que deseja visualizar -> "))
            elif(create_new == 3):
                print("Retornando ao menu anterior.")
                voltar = True
            else:
                print("Opção inexistente.")
                ##voltar = True

def create_personagem():
    print("========== <> ==========")
    nome = input("Nome Personagem: ")
    raca = input("Raça: ")
    classe = input("Classe: ")
    dados_personagem.new_personagem(nome,raca,classe)


def atributos_personagem(index):
    print("========== <> ==========")
    print("ATRIBUTOS")
    pontos_total = dados_personagem.nivel_personagem[index] + 19
    print("Total de pontos a distribuir: {}".format(pontos_total))

    voltar = False

    while(not voltar):

        strenght = int(input("Força: "))
        dexterity = int(input("Destreza: "))
        inteligence = int(input("Inteligência: "))
        constitution = int(input("Constituição: "))
        wisdown = int(input("Sabedoria: "))
        charism = int(input("Carisma: "))

        pontos = dados_personagem.personagem_atributos(index,strenght,dexterity, inteligence,constitution,wisdown,charism)

        if(pontos < 0):
            print("Distribuido {} pontos indevidamente.".format(pontos))
        else:
            not_error = False
            while(not not_error):
                print("Pontos distribuidos: {} de {}.".format(pontos_total - pontos,    pontos_total))
                confirm_atrib = int(input("Confirmar?\n| 1-Sim\n| 2-Não\n"))
            
                if(confirm_atrib == 1):
                    print("Atributos confirmados.")
                    not_error = True
                    voltar = True
                elif(confirm_atrib == 2):
                    print("Reiniciar distribuição.")
                    not_error = True
                else:
                    print("Opção incorreta.")
                    


if(__name__ == "__main__"):
    menu()