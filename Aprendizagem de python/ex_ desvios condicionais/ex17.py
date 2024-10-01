preço = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual do desconto: "))
preço_final = preço * (1 - (desconto/100))
print("O preço final do produto é: ", preço_final)