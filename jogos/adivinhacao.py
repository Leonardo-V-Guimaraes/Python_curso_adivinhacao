import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentivas = 0
pontos = 20

print("Selecione o nível de dificuldade", numero_secreto)
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Define o nível: "))

if(nivel == 1):
    total_de_tentivas = 20
elif(nivel == 2):
    total_de_tentivas = 10
else:
    total_de_tentivas = 5

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
        if(chute_maior):
            print("Você errou! O seu chute foi maior do que o número secreto.""\n")
            if (rodada == total_de_tentivas):
                print("O numero secreto era {}. Você fez {} pontos""\n".format(numero_secreto, pontos))
        elif(chute_menor):
            print("Você errou! O seu chute foi menor do que o número secreto.""\n")
            if (rodada == total_de_tentivas):
                print("O numero secreto era {}. Você fez {} pontos""\n".format(numero_secreto, pontos))
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos 


print ("Fim do jogo!")