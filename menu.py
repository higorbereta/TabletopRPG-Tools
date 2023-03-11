import personagem

def menu():

    print("Bem vindo ao Tabletop RPG Tool")

    encerrar = False

    while(not encerrar):

        print(" 1 - Ficha de Personagem\n 2 - Dado \n 0 - Encerrar")
        menu_option = int(input("Selecione a opção desejada -> "))
        
        if(menu_option == 1):
            personagem.ficha_personagem()
        if(menu_option == 2):
            print("Dado")
        if(menu_option == 0):
            print("Encerrando aplicação")
            encerrar = True

if(__name__ == "__main__"):
    menu()