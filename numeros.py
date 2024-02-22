import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 6

    print("Bem-vindo ao jogo de adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")

    while tentativas < max_tentativas:
        palpite = int(input("Digite o seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("O número secreto é maior que", palpite)
        elif palpite > numero_secreto:
            print("O número secreto é menor que", palpite)
        else:
            print("Parabéns! Você acertou o número secreto em", tentativas, "tentativas.")
            break
    else:
        print("Você não conseguiu adivinhar o número secreto em 6 tentativas. O número era", numero_secreto)

jogo_adivinhacao()
