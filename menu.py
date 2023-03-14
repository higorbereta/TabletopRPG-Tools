import dados_personagem

def menu():

    print("Bem vindo ao Tabletop RPG Tool")

    encerrar = False

    while(not encerrar):

        print(" 1 - Ficha de Personagem\n 2 - Dado \n 0 - Encerrar")
        menu_option = int(input("Selecione a opção desejada -> "))
        if(menu_option == 1):
            ficha_personagem()
        elif(menu_option == 2):
            print("Dado")
        elif(menu_option == 0):
            print("Encerrando aplicação")
            encerrar = True
        else:
            print("Opção não identificada.")
            
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
                voltar = True
            elif(create_new == 2):
                num_personagem = int(input("Número do personagem que deseja visualizar -> "))
                exibe_personagem(num_personagem)
                option_ficha = int(input("Opções:\n| 1-Distribuir Atributos\n| 2-Acrescentar EXP\n"))
                if(option_ficha == 1):
                    atualiza_atributos(num_personagem)
                    exibe_atributos(num_personagem)
                voltar = True
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
    especialidade = input("Especialização: ")
    dados_personagem.new_personagem(nome,raca,classe,especialidade)


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

def atualiza_atributos(index):

    nome_atrib = int(input("Qual o atributo que deseja aumentar?\n| 1-Força\n| 2-Destreza\n| 3-Inteligência\n| 4-Constituição\n| 5-Sabedoria\n| 6-Carisma\n"))

    limite = True

    while(limite):
        qnt_pts = int(input("Pontos a adicionar: "))
        if(nome_atrib == 1):
            ##print("strenght")
            limite,message = dados_personagem.update_atributos(index,"strenght",qnt_pts)
            ##print(message)
        elif(nome_atrib == 2):
            ##print("dexterity")
            limite,message = limite,message = dados_personagem.update_atributos(index,"dexterity",qnt_pts)
        elif(nome_atrib == 3):
            ##print("inteligence")
            limite,message = dados_personagem.update_atributos(index,"inteligence",qnt_pts)
        elif(nome_atrib == 4):
            ##print("constitution")
            limite,message = dados_personagem.update_atributos(index,"constitution",qnt_pts)
        elif(nome_atrib == 5):
            ##print("wisdown")
            limite,message = dados_personagem.update_atributos(index,"wisdown",qnt_pts)
        elif(nome_atrib == 6):
            ##print("charism")
           limite,message =  dados_personagem.update_atributos(index,"charism",qnt_pts)
        else:
            print("Opção inexistente.")

        if(message == "Error"):
            print("Pontuação acima do permitido.")
        else:
            print("Atributo aumentado com sucesso !!")
            ##exibe_atributos(index)



def exibe_personagem(index):
    print("========== <> ==========")
    print("DADOS DO PERSONAGEM")
    print("Nome: {}".format(dados_personagem.nome_personagem[index]))
    print("Raça: {}".format(dados_personagem.raca_personagem[index]))
    print("Classe: {}".format(dados_personagem.classe_personagem[index]))
    print("Nível: {}".format(dados_personagem.nivel_personagem[index]))
    print("Exp: {}/{}".format(dados_personagem.exp_personagem[index],dados_personagem.next_level[index]))

    exibe_atributos(index)

    

def exibe_atributos(index):
    print("========================")
    
    print("Força: {}".format(dados_personagem.atributos_personagem[index]['strenght']))
    print("Destreza: {}".format(dados_personagem.atributos_personagem[index]['dexterity']))
    print("Inteligência: {}".format(dados_personagem.atributos_personagem[index]['inteligence']))
    print("Constituição: {}".format(dados_personagem.atributos_personagem[index]['constitution']))
    print("Sabedoria: {}".format(dados_personagem.atributos_personagem[index]['wisdown']))
    print("Carisma: {}".format(dados_personagem.atributos_personagem[index]['charism']))
    print("|  Pontos disponíveis: {}".format(dados_personagem.pontos_atributos(index)))

    print("========== <> ==========")

if(__name__ == "__main__"):
    menu()