from operator import le
import random

def jogar():

    print("**********************************")
    print("**Bem vindo ao jogo de da forca!**")
    print("**********************************""\n")

    with open("palavras.txt") as arquivo: # O uso do with substitui a necessidade de ter que dar um .close() ele faz isso por padrão
        palavras = [] # Criar a lista

        for linha in arquivo:
            linha = linha.strip() #Strip retira os caracteres especiais como \n.
            palavras.append(linha) #palavras adiciona linha

    numero = random.randrange(0, len(palavras)) # O 0 é o valor inicial da lista, adicionando +1 para cada elemento usando o len
    palavra_secreta = palavras[numero].upper() # Palavra_secreta usa o numero que possua um randomizador e o .upper() para deixar as palavras em maisculo
    letras_acertadas = ["_" for letra in palavra_secreta] #List Comprehension - Compreensão de listma
   
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #Enquanto(TRUE)
    while(not enforcou and not acertou):

        chute = input("Qual letra? ").upper().strip()[0] #chute = chute.strip().upper() - Fazendo o código mais facil de ler

        if(chute in palavra_secreta):

            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1 # += Mesma função de adicionar +1
        else:
            print("Ops! você errou! Ainda tem {} chances.".format(5-erros))
            erros += 1 # += Mesma função de adicionar +1

        if(erros == 6):
            break
        if("_" not in letras_acertadas):
            break
        print(letras_acertadas)            

    if("_" not in letras_acertadas): #Faz a leitura do "_", caso não tenha essa sequencia ele termina o jogo
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo a palavra é {}.".format(palavra_secreta))

""" Este if faz com que o arquivo forca.py seja executado sem o jogos.py...
motivo... Quando ele é executado ele gera um arquivo chamado __main__, por isso ...
o __name__ ==. Fazendo com isso ele executar a função jogar() quando existe um import para ...
outro arquivo."""
if(__name__ == "__main__"):
    jogar()