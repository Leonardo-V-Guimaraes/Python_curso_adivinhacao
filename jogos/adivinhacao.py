import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentivas = 0
    pontos = 1000

    print("Selecione o nível de dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_de_tentivas = 20
    elif(nivel == 2):
        total_de_tentivas = 10
    elif(nivel == 3):
        total_de_tentivas = 5
    else:
        print("O nível dever ser entre 1 2 3")

    for rodada in range(1, total_de_tentivas + 1):
        print("\n""Tentativa {} de {}".format(rodada, total_de_tentivas,"\n"))
        chute_str = input("Digite o seu numero: ")
        print("Você digitou: " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve escolher um número entre 1 e 100!""\n")
            continue

        acertou     = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!""\n".format(pontos))
            break
        else: 
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos 
            if(chute_maior):
                print("Você errou! O seu chute foi maior do que o número secreto.""\n")
                if (rodada == total_de_tentivas):
                    print("O numero secreto era {}. Você fez {} pontos""\n".format(numero_secreto, pontos))
            elif(chute_menor):
                print("Você errou! O seu chute foi menor do que o número secreto.""\n")
                if (rodada == total_de_tentivas):
                    print("O numero secreto era {}. Você fez {} pontos""\n".format(numero_secreto, pontos))



    print ("Fim do jogo!")

# Este if faz com que o arquivo adivinhacao.py seja executado sem o jogos.py...
# motivo... Quando ele é executado ele gera um arquivo chamado __main__, por isso ...
# o __name__ ==. Fazendo com isso ele executar a função jogar() quando existe um import para ...
# outro arquivo.
if(__name__ == "__main__"):
    jogar()