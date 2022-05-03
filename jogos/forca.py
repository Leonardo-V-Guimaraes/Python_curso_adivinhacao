from operator import le


def jogar():

    print("**********************************")
    print("**Bem vindo ao jogo de da forca!**")
    print("**********************************")

    palavra_secreta = "baanana".upper()
    letras_acertadas = ["_","_","_","_","_","_"]
   
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #Enquanto(TRUE)
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        if(chute in palavra_secreta):

            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                    # += Mesma função de adicionar +1
                index += 1 
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)            

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")

""" Este if faz com que o arquivo forca.py seja executado sem o jogos.py...
motivo... Quando ele é executado ele gera um arquivo chamado __main__, por isso ...
o __name__ ==. Fazendo com isso ele executar a função jogar() quando existe um import para ...
outro arquivo."""
if(__name__ == "__main__"):
    jogar()