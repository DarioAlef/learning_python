#Q.05 - Peça um número e use um laço para exibir sua tabuada de 1 a 10

num = int(input('Digite um número inteiro qualquer: '))

print('\nA tabuada desse número é: ')
for i in range(0, 10):
    i+=1
    resultado = i * num
    print(f'\n{num} x {i} = {resultado}')