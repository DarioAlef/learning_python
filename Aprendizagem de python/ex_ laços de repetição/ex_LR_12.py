#Q.12 - peça um número e imprima quantos dígitos ele possui

num = int(input('\nDigite um número inteiro qualquer: '))

count = 0

<<<<<<< HEAD
while num > 1:         # antes com 'num / 10', a variável 'num' não recebia o valor
    num = num / 10     # ou seja, a cada novo laço, num voltava para o seu valor original
    count+=1           # por isso estava em um laço infinito
print(count)
