#Q.05 - leia o número de dias que um funcionário trabalhou e calcule seu salário, considerando um valor por hora

dias = int(input('\nDigite o total de dias trabalhados: '))
valor = float(input('Digite o valor da hora trabalhada: '))
salario = dias * (valor * 8)

print(f'\nSeu salário é de R${salario:.2f}\n')