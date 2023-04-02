import random

numero_maximo = 100
numero_aleatorio = random.randint(1, numero_maximo)

while True:
    resposta = int(input("Adivinhe o número entre 1 e {}: ".format(numero_maximo)))

    if resposta < numero_aleatorio:
        print("O número é maior!")
    elif resposta > numero_aleatorio:
        print("O número é menor!")
    else:
        print("Parabéns, você acertou!")
        break

print("Fim do jogo!")