from operator import le
import random

def jogar(): # Definir Função

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta) # utilizando o palavra secreta como parametro
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    #Enquanto(TRUE)
    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta) #busca as 3 variaveis necessarias
        else:
            print("Ops! você errou! Tem {} chances.".format(6-erros))
            erros += 1 # += Mesma função de adicionar +1
            desenha_forca(erros)

        if(erros == 7):
            break
        if("_" not in letras_acertadas):
            break
        print(letras_acertadas)            

    if("_" not in letras_acertadas): #Faz a leitura do "_", caso não tenha essa sequencia ele retorna mensagem de vencedor
        imprime_mensagem_vencedor(palavra_secreta) 
    else:
        imprime_mensagem_perdedor(palavra_secreta)

#Funções#

def imprime_mensagem_abertura():

    print("**********************************")
    print("**Bem vindo ao jogo de da forca!**")
    print("**********************************""\n")

def carrega_palavra_secreta():

    print("(1) Frutas (2) Cores") 
    lista_de_jogo = int(input("escolha qual lista deseja: ")) # Convertendo para INT, passando pela comparação a baixo
    # Lembrando que quando for para fazer uma comparação entre STR(string) - numero, deve converter o STR para INT
    if (lista_de_jogo == 1):
        print("\n""Frutas!")
        lista_de_jogo = "frutas.txt"
    elif (lista_de_jogo == 2):
        print("\n""Cores!")
        lista_de_jogo = "cores.txt"

    with open(lista_de_jogo) as arquivo: # O uso do with substitui a necessidade de ter que dar um .close() ele faz isso por padrão
        palavras = [] # Criar a lista

        for linha in arquivo:
            linha = linha.strip() #Strip retira os caracteres especiais como \n.
            palavras.append(linha) #palavras adiciona linha

    numero = random.randrange(0, len(palavras)) # O 0 é o valor inicial da lista, adicionando +1 até o final da lista "len"
    palavra_secreta = palavras[numero].upper() # Palavra_secreta usa o numero que possua um randomizador e o .upper() para deixar as palavras em maisculo
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]
    ## ["_" for letra in palavra_secreta] #List Comprehension - Compreensão de listma

def pede_chute():
    chute = input("Qual letra? ").upper().strip()[0] #chute = chute.strip().upper() - Fazendo o código mais facil de ler
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta): # manda as 3 variaveis necessarias
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1 # += Mesma função de adicionar +1

def imprime_mensagem_vencedor(palavra_secreta):
    print("Parabéns você acertou! A palavra é {}.".format(palavra_secreta))
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {} !".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

""" Este if faz com que o arquivo forca.py seja executado sem o jogos.py...
motivo... Quando ele é executado ele gera um arquivo chamado __main__, por isso ...
o __name__ ==. Fazendo com isso ele executar a função jogar() quando existe um import para ...
outro arquivo."""
if(__name__ == "__main__"):
    jogar()