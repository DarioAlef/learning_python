#07 - receba o ano de nascimento de uma pessoa e calcule quantos anos, meses e dias ela tem

nascimento = int(input('\nDigite o ano de nascimento: '))

idade = 2022 - nascimento

print(f'\nSua idade é de {idade} anos, {idade*12} meses e {idade*365} dias\n')