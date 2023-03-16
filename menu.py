import dados_personagem
import random
import calc_rpg

def menu():

    print("Bem vindo ao Tabletop RPG Tool")

    encerrar = False

    while(not encerrar):

        print(" 1 - Ficha de Personagem\n 2 - Dado\n 3 - Calculadora \n 0 - Encerrar")
        menu_option = option()
        if(menu_option == 1):
            ficha_personagem()
        elif(menu_option == 2):
            ##print("Dado")
            menu_dado(1) ## Origem 1 para informar que o acesso veio do Menu
        elif(menu_option == 3):
            calculadora(False,0) ## Envia sinal False e dado 0 para sinalizar que o dado não foi rodado
        elif(menu_option == 0):
            print("Encerrando aplicação")
            encerrar = True
        else:
            print("Opção não identificada.")



def menu_dado(origem):
    lados = int(input("Quantidade de lados -> "))
    result_dado = roda_dado(lados)
    print(" ----- ")
    print("|  {}  |".format(result_dado))
    print(" -----")

    if(origem == 1): ## Valida se a execução do método veio pelo Menu pra perguntar se quer a execução da calculadora
        print("Calculadora?\n| 1-Sim\n| 2-Não")
        habilita_calc = option()
        if(habilita_calc == 1):
            calculadora(True,result_dado)
    else:
        return result_dado

def roda_dado(lados):
    valor_dado = random.randrange(1,lados)
    
    return valor_dado

def option(): ## Método padrão de input para encurtar o código
    escolha = int(input("Seleciona a opção desejada -> "))
    return escolha
        

def calculadora(dado_rodado,resultado_dado):
    print("+++++++++++++++++++ ")
    print("CALCULADORA RPG")

    if(not dado_rodado): ## Sinal False na chamada do método indica que o dado não foi executado, e inicia a execução
        valor_dado = menu_dado(2) ## Origem 2 sinaliza que a execução veio da calculadora

    voltar = False

    while(not voltar):
        print("| 1-Calculadora de Dano\n| 2-Calculadora de Acerto\n| 3-Teste de Atributos\n| 0-Fechar Calculadora")
        option_calc = option()
        if(option_calc == 1):
            print("Calcular DANO")
        elif(option_calc == 2):
            print("Calcular Acerto")
        elif(option_calc == 3):
            ##print("TESTE DE ATRIBUTOS")

            print("Qual o personagem testado?\n{}".format(dados_personagem.nome_personagem))
            personagem_teste = int(option())

            max_personagem = len(dados_personagem.nome_personagem)

            if(personagem_teste > 0 and personagem_teste <= max_personagem):
                confirm_atrib = False
                while(not confirm_atrib):
                    print("Atributo que será testado:\n| 1-Força\n| 2-Destreza\n| 3-Inteligência\n| 4-Constituição\n| 5-Sabedoria\n| 6-Carisma\n| 0-Cancelar")
                    atrib_option = int(option())
                    if(atrib_option > 0 and atrib_option <=6):
                        confirm_atrib = True
                        dificuldade = int(input("Dificuldade do teste -> "))
                        print("Resultado do teste: {}".format(calc_rpg.atrib_teste(atrib_option,dificuldade,personagem_teste, valor_dado)))
                        voltar = True
                    elif(atrib_option == 0):
                        print("Teste cancelado.")
                        confirm_atrib = True
                    else:
                        print("Atributo inválido.")
            else:
                print("Personagem inexistente.")
        elif(option_calc == 0):
            voltar = True
        else:
            print("Opção invalida!")
            
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
            print("Deseja criar um novo personagem ou Acessar uma ficha?\n| 1-Acessar uma ficha\n| 2-Criar novo Personagem\n| 3-Voltar")
            create_new = option()
            
            if(create_new == 1):
                num_personagem = int(input("Número do personagem que deseja visualizar -> "))
                exibe_personagem(num_personagem)
                print("Opções:\n| 1-Acrescentar EXP\n| 2-Distribuir Atributos")
                option_ficha = option()
                
                if(option_ficha == 1):
                    pts_exp = int(input("Valor de EXP a acrescentar -> "))
                    level_up = dados_personagem.update_exp(num_personagem, pts_exp)
                    if(level_up == True):
                        print("Level UP!!!")
                        print("Novos pontos de atributos disponíveis.")
                elif(option_ficha == 2):
                    atualiza_atributos(num_personagem)
                    exibe_atributos(num_personagem)
                voltar = True
            elif(create_new == 2):
                print("Iniciando criação novo personagem.")
                create_personagem()
                last_personagem = len(dados_personagem.nome_personagem)
                atributos_personagem(last_personagem)
                print("Personagem {} criado.".format(last_personagem))
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

    print("Qual o atributo que deseja aumentar?\n| 1-Força\n| 2-Destreza\n| 3-Inteligência\n| 4-Constituição\n| 5-Sabedoria\n| 6-Carisma")
    nome_atrib = option()

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