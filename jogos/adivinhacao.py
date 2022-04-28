print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentivas = 3

for rodada in range(1, total_de_tentivas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentivas,"\n"))
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
        print("Você acertou!""\n")
        break
    else: 
        if(chute_maior):
            print("Você errou! O seu chute foi maior do que o número secreto.""\n")
        elif(chute_menor):
            print("Você errou! O seu chute foi menor do que o número secreto.""\n")

print ("Fim do jogo!")