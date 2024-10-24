#Q.04 - leia três notas e calcule a média ponderada.

n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
m = (n1*2 + n2*3 + n3*5) / 10
print(f'\nSua média ponderada é {m:.1f}\n')