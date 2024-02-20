def determinar_estacao(mes):
    # Dicionário com os intervalos de meses para cada estação
    estacoes = {
        "janeiro": "Verão",
        "fevereiro": "Verão",
        "março": "Verão",
        "abril": "Outono",
        "maio": "Outono",
        "junho": "Outono",
        "julho": "Inverno",
        "agosto": "Inverno",
        "setembro": "Primavera",
        "outubro": "Primavera",
        "novembro": "Primavera",
        "dezembro": "Verão"
    }

    # Verifica em qual estação o mês se encaixa
    mes_lower = mes.lower()
    if mes_lower in estacoes:
        return estacoes[mes_lower]
    else:
        return "Mês inválido"

# Solicita ao usuário o nome do mês
mes_digitado = input("Digite o nome do mês: ")

# Calcula a estação correspondente ao mês
estacao_correspondente = determinar_estacao(mes_digitado)

# Imprime a estação correspondente
print(f"O mês {mes_digitado.capitalize()} corresponde à estação {estacao_correspondente}.")


