import forca
import adivinhacao

def escolhe_jogo():
    print("**********************************")
    print("********Escolha seu jogo!*********")
    print("**********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo!?"))

    if (jogo == 1):
        print("\n""Jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("\n""Jogando Adivinhação")
        adivinhacao.jogar()

    print ("Fim do jogo!")

if(__name__ == "__main__"):
    escolhe_jogo()