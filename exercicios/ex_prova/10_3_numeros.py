#Q.10 - leia três números reais e exiba o maior, o menor e a diferença entre eles

n1 = float(input('\nDigite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

lista = [n1, n2, n3]

maior = max(lista)
menor = min(lista)
diferenca = maior - menor

print(f'\nO maior número é {maior:.2f}\nO menor número é {menor:.2f}\nA diferença entre esses números é {diferenca:.2f}\n')