def function_soma(num1, num2, num3):
  soma = num1 + num2 + num3
  return soma

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))

print(f'\nA soma é: {function_soma(num1, num2, num3)}')