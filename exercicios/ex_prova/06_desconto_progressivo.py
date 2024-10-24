#Q.06 -  receba o valor de um produto e aplique um desconto progressivo de acordo com a quantidade comprada

valor_produto = float(input('\nDigite o valor do produto: '))
quantidade = int(input('Digite a quantidade peças: '))
desconto = 1 - (quantidade * (5/100))

print(f'\nO valor final do seu produto é de R$ {valor_produto * desconto:.2f}\n')

#+1 peça = +5% de desconto
