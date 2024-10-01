# Q.09 - peça e calcule o fatorial de um número (produto dele pelos seus antecessores maiores que 0)

# Solicita o número ao usuário
numero = int(input("Digite um número para calcular o fatorial: "))

# Inicializa a variável para armazenar o fatorial
fatorial = 1

# Verifica se o número é válido
if numero < 0:
    print("Fatorial não definido para números negativos.")
else:
    # Calcula o fatorial usando um loop for
    for i in range(1, numero + 1):  #começa em 1 e vai somando 1 a número
        fatorial *= i
        #4 --> fatorial = 1 * 1 --> fatorial = 1
        #      fatorial = 1 * 2 --> fatorial = 2
        #      fatorial = 2 * 3 --> fatorial = 6
        #      fatorial = 6 * 4 --> fatorial = 24

    # Imprime o resultado
    print(f"O fatorial de {numero} é {fatorial}")