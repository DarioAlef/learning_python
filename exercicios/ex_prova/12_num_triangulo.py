#12 - verifique se três números podem formar os lados de um triângulo retângulo

n1 = int(input('\nDigite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))


if n1 != n2 and n1 != n3 and n2 != n3:
    print(f'\nAs lados {n1}, {n2} e {n3} formam um triângulo retângulo\n')
else:
    print(f'\nAs lados {n1}, {n2} e {n3} NÃO formam um triângulo retângulo\n')