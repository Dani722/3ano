nota01 = float(input("Digite a nota do PRIMEIRO bimestre: "))
nota02 = float(input("Digite a nota do SEGUNDO bimestre: "))
nota03 = float(input("Digite a nota do TERCEIRO bimestre: "))
nota04 = float(input("Digite a nota do QUARTO bimestre: "))

media = (nota01 + nota02 + nota03 + nota04) / 4

print("A média final é:", media)

if media >= 7:
    print("Aprovado")
else:
    print("Não Aprovado")
