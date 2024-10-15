#Q.13 - peça ao usuário para inserir 10 números e some-os

soma = 0

for j in range(1, 11):
    j = int(input('\nDigite um número inteiro qualquer: '))
    soma = soma + j

print(f'A soma de todos esses números é: {soma}\n')