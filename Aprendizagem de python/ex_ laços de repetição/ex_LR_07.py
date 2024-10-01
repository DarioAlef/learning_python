# Q.07 - Calcule a soma de todos os números pares de 1 a 100
soma = 0
for i in range(0,101,2):
    soma = soma + i
print(f'A soma de todos os números pares de 1 até 100 é: {soma}')