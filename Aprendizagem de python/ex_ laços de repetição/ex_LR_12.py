#Q.12 - peça um número e imprima quantos dígitos ele possui

num = int(input('\nDigite um número inteiro qualquer: '))

count = 0

while num > 0:
    num / 10
    count+=1
    print(count)
    break
