#Q.02 -  leia o nome completo de uma pessoa e exiba apenas o primeiro e o último nome

nome = str(input('\nDigite o seu nome completo: '))

nome = nome.split(' ')

print(f'\nSeu primeiro nome é \'{nome[0]}\' e seu último nome é \'{nome[-1]}\'\n')
