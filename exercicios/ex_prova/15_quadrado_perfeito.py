#Q.15 - leia um número e determine se ele é um quadrado perfeito

num = int(input('\nDigite um número: '))

for i in range(1, num):
    if i * i == num:      #if algum número vezes ele mesmo é igual a 'num', então é quadrado perfeito                             
        print(f'\n{num} é um quadrado perfeito\n')
        break
    elif i == num - 1:
        print(f'\n{num} NÃO é um quadrado perfeito\n')

#o loop é necessário para testar diferentes números da raíz, e como uma
#raíz é o inverso de um exponte, então 'i*i'