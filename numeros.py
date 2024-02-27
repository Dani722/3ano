import random

def jogo_adivinhacao():
    
    nível = int(input("Escolha o nível de dificuldade (1- Fácil, 2- Médio, 3- Díficil): "))
    max_numero = 10 if nível == 1 else 50 if nível == 2 else 100
    numero_secreto = random.randint(1, max_numero)
    tentativas = 10 if nível == 1 else 5 if nível == 2 else 3
    pontos = 1000

    print(f"Jogo de Adivinhação - Nível {nível}")
    print(f"Estou pensando em um número entre 1 e {max_numero}.")
    
    for tentativa  in range (1, tentativas + 1):
        print(f"Tentativa {tentativa} de {tentativas}")
        palpite = int(input("Digite seu palpite: "))
        
        if palpite < 1 or palpite > max_numero:
            print(f"Digite um número entre 1 e {max_numero}.")
            continue
        
        acertou = palpite == numero_secreto
        maior = palpite > numero_secreto
        menor = palpite < numero_secreto
        
        if acertou:
            print(f"Voce acertou e fez {pontos} pontos!")
            break
        else:
            pontos_perdidos = abs(numero_secreto - palpite)
            pontos -= pontos_perdidos
            if maior:
                print("seu palpite foi maior que o numero secreto.")
            elif menor:
                print("seu palpite foi menor que o numero secreto.")
                
    if not acertou:
        print(f"Suas tentativas acabaram. O numero secreto era {numero_secreto}.")
        print("Fim do Jogo!")
        
if __name__ == "__main__":
    jogo_adivinhacao()
