#Q.17 - calcule a soma dos números pares de 1 a 1000

soma = 0

for i in range(1001):
    if i % 2 == 0:
        soma += i
print(f'\n{soma}\n')