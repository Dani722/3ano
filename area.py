def area_circulo(raio):
    return 3.14159 * raio ** 2

raio = float(input("Digite o raio do círculo: "))
print(f"A área do círculo é: {area_circulo(raio)}")


def area_quadrado(lado):
    return lado ** 2

lado = float(input("Digite o comprimento do lado do quadrado: "))
print(f"A área do quadrado é: {area_quadrado(lado)}")


def area_triangulo(base, altura):
    return 0.5 * base * altura

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
print(f"A área do triângulo é: {area_triangulo(base, altura)}")
