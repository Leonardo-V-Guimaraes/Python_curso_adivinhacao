print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")

print("Você digitou " , chute_str)

chute = int(chute_str)

acertou     = chute == numero_secreto
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto

if (acertou):
    print("Você acertou!")
else: 
    if(chute_maior):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif(chute_menor):
        print("Você errou! O seu chute foi menor do que o número secreto.")
print ("Fim do jogo!")