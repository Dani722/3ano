import random

def jogar_jokenpo():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    print("Bem vindo ao jogo!")
    print("Escolha: pedra, papel, tesoura")

    while True:
        escolha_jogador = input("Sua escolha:")
        if escolha_jogador not in opcoes:
            print("Eschola inválida, Tente Novamente.")
            continue

        escolha_computador = random.choice(opcoes)

        print(f"Computador escolheu: {escolha_computador}")

        if escolha_jogador == escolha_computador:
            print("Empate!")
        elif(
            (escolha_jogador == "Papel" and escolha_computador == "Pedra") or
            (escolha_jogador == "Pedra" and escolha_computador == "Tesoura") or
            (escolha_jogador == "Tesoura" and escolha_computador == "Papel")):
            print("Você venceu!")
        else:
            print("Você perdeu!")

        jogar_novamente = input("Você quer jogar novamente?")
        if jogar_novamente != "sim":
            break

if __name__== "__main__":
    jogar_jokenpo()