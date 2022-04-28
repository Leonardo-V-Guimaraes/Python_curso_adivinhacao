print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentivas = 3
rodada = 1

while(rodada <= total_de_tentivas):
    print("Tentativa {} de {}".format(rodada, total_de_tentivas,"\n"))
    chute_str = input("Digite o seu numero: ")
    print("Você digitou: " , chute_str)
    chute = int(chute_str)

    acertou     = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!""\n")
        rodada = 3
    else: 
        if(chute_maior):
            print("Você errou! O seu chute foi maior do que o número secreto.""\n")
        elif(chute_menor):
            print("Você errou! O seu chute foi menor do que o número secreto.""\n")

    rodada = rodada + 1

print ("Fim do jogo!")