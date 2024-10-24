#Q.08 - simule uma calculadora financeira de juros simples e compostos

# JUROS SIMPLES: j = c * i * t
# JUROS COMPOSTOS: m = c * (1 + i)^n
         # c + j = c * (1 + i)^n

def menu():
    print('\n[1] Juros simples')
    print('[2] Juros compostos')
    escolha = int(input('\nEscolha uma das opções que deseja calcular: '))
    
    if escolha == 1:
        return juros_simples()
    elif escolha == 2:
        return juros_compostos()
    else:
        print('Escolha uma opção valida!')
    return 

def juros_simples():
    index = float(input("\nDigite o valor do juros: "))
    capital = float(input("Digite o valor do capital: "))
    tempo = int(input("Digite o tempo em meses: "))
    juros = capital * (index/100) * tempo
    print('\nO que será apenas de juros simples é: {juros:.2f}')
    print(f'O valor total que será pago é {(capital + juros):.2f}\n')
    
def juros_compostos():
    index = float(input("\nDigite o valor do juros: "))
    capital = float(input("Digite o valor do capital: "))
    tempo = int(input("Digite o tempo em meses: "))
    juros = (capital * (1 + index/100) ** tempo) - capital
    print(f'\nO que será pago apenas de juros compostos é: {juros:.2f}')
    print(f'O valor total que será pago é {(capital + juros):.2f}\n')
    
if __name__ == '__main__':
    menu()