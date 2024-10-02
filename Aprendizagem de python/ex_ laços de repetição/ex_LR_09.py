# Q.09 - peça e calcule o fatorial de um número (produto dele pelos seus antecessores maiores que 0)

num = int(input('\nDigite um número inteiro qualquer: '))

fatorial = 1

if num == 1:
    print('\nO fatorial de 1 é \'1\'\n')

elif num < 0: 
    print('Digite apenas um número positivo')

elif num == 0:
    print('\n0 não é um número válido, digite apenas um número positivo\n')

else:
    for i in range(1, num + 1):
        fatorial *= i
    print(f'\nO fatorial de {num} é {fatorial}\n')