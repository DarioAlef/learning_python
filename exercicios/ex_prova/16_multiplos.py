#16 - leia dois números e verifique se o segundo é múltiplo do primeiro

n1 = int(input('\nDigite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n2 % n1 == 0:
    print(f'\n{n2} é múltiplo de {n1}\n')
else:
    print(f'\n{n2} NÃO é múltiplo de {n1}\n')

# múltiplo = 'divisível'