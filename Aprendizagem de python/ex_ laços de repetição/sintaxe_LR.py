# WHILE: equivalente ao 'enquanto e o 'faca enquanto'. Usado para quando não se tem um fim definindo 
num = 1
while (num <= 10):
    print(num)
    num += 1
print('Laço encerrado') #identação é muito importante em Python

nome = None    #'None' especifica uma variável do tipo vazio
while True:    #'True' faz com que o laço aconteça de qualquer jeito
    nome = input('Digite o seu nome ou \'x\' para parar: ')
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem-vindo, {nome}')


#FOR: equivale ao 'para'. Usado quando se tem um fim definido
lista1 = [0,1,2,3,4,5]
for item in lista1:  #'para a variável item dentro da lista1'
    print(item)

print('\n')

palavra = 'Bóson'
for letra in palavra:
    print(letra)


# FOR - RANGE: range significa 'faixa', estabelece uma delimitação para a repetição
for número in range(1, 5):
    print(número,'\t')

nome2 = 'Bacate'
for x in range(5):
    print(f'{x+1} {nome2}')

for k in range(0, -21, -4): #respectivamente: valor inicial, valor inicial, incremento (de 4 em 4)
    print(k)

print('\n')

pedras_preciosas = ('rubi','diamante','esmeralda','topázio')  #TUPLA
for pedras in pedras_preciosas:
    if pedras == 'esmeralda':
        continue  #encerra a identação atual, encerra a roda atual do laço
    print(pedras)

#laços encadeados
for contador_externo in range(1,6):
    print(f'\nRodadado {contador_externo}')
    for contador_interno in range(1,4):
        print(f'Valor: {contador_interno}')

import random
for a in range(1,6):
    print(f'\nConjunto {a}')
    for b in range(5):  # rode 5 vezes independente dos valores 
        num = random.randint(1,100)  #um número aleatório inteiro entre 1 e 100
        print(f'Valor {num}')
