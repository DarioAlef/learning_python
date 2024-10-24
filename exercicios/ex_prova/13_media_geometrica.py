#Q.13 - calcule a média aritmética e a média geométrica de quatro números

count = 1
soma = 0
media_arit = soma / count
media_geom = (soma ** (1/count))
num = float(input('\nDigite um número maior que zero: '))

while num > 0:
    num = float(input('Digite outro número maior que zero: '))
    if num > 0:
        count += 1
        soma += num
        media_arit = soma / count
        media_geom = (soma ** (1/count))
print(f'\nA média aritmetica desses números é {media_arit:.2f}\nA média geométrica é {media_geom:.2f}\n')