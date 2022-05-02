def jogar():

    print("**********************************")
    print("**Bem vindo ao jogo de da forca!**")
    print("**********************************")

    palavra_secreta = "banana"
   
    enforcou = False
    acertou = False

    #Enquanto(TRUE)
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
    
        print("jogando...")
    print("Fim do jogo")

# Este if faz com que o arquivo forca.py seja executado sem o jogos.py...
# motivo... Quando ele é executado ele gera um arquivo chamado __main__, por isso ...
# o __name__ ==. Fazendo com isso ele executar a função jogar() quando existe um import para ...
# outro arquivo.
if(__name__ == "__main__"):
    jogar()