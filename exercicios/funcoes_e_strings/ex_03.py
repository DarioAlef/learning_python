#Q.3 - Faça uma função que receba três argumentos, e que forneça a soma desses três

def soma(num1, num2, num3):
    resultado = num1 + num2 + num3
    return resultado
    
num1 = int(input('\nDigite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))

print(f'\nA soma é: {soma(num1, num2, num3)}\n')