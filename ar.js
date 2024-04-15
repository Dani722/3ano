nome = ["Ana", "Bruno", "Carlos", "Daniel", "Eduardo"]
idade = [25, 30, 35, 40, 45]

console.log(`o ${nome[0]} tem ${idade[0]} anos`)
console.log(`o ${nome[1]} tem ${idade[1]} anos`)
console.log(`o ${nome[2]} tem ${idade[2]} anos`)
console.log(`o ${nome[3]} tem ${idade[3]} anos`)
console.log(`o ${nome[4]} tem ${idade[4]} anos`)


import 'dart:io';

void main() {
  print("Digite o primeiro número:");
  double num1 = double.parse(stdin.readLineSync()!);

  print("Digite o segundo número:");
  double num2 = double.parse(stdin.readLineSync()!);

  print("Digite a operação (+, -, *, /):");
  String operacao = stdin.readLineSync()!;

  double resultado;

  switch (operacao) {
    case '+':
      resultado = num1 + num2;
      break;
    case '-':
      resultado = num1 - num2;
      break;
    case '*':
      resultado = num1 * num2;
      break;
    case '/':
      if (num2 != 0) {
        resultado = num1 / num2;
      } else {
        print("Erro: Divisão por zero não é permitida.");
        return;
      }
      break;
    default:
      print("Operação inválida. Use +, -, *, ou /.");
      return;
  }

  print("Resultado: $resultado");
}
