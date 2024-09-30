capital = float(input("Digite o valor do capital: "))
tx_juros = float(input("Digite a taxa de juros: "))
tempo = int(input("Digite a quantidade de meses: "))

juros = capital * (tx_juros/100) * tempo

print("O juros simples é: ", juros)