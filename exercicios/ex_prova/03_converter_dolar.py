#Q.03 - converta reais para dólares, com a cotação atual informada pelo usuário.

def menu():
    escolha = int(input('\n\n[1] Real para Dólar\n[2] Dólar para Real\n\nEscolha a opção desejada: '))
    
    if escolha == 1:
       return converter_real_dolar()
    elif escolha == 2:
        return converter_dolar_real()
    else:
        print('Opção inválida!')
    return escolha  

def converter_real_dolar():
    dinheiro = float(input('\ndigite o valor em reais que deseja converter para dólares: '))
    cotacao = float(input('digite a cotação do dolar atual: '))
    return print(f'\nR${dinheiro} em dolares equivale a ${dinheiro/cotacao:.2f}\n')
    
def converter_dolar_real():
    dinheiro = float(input('\ndigite o valor em dolares que deseja converter para reais: '))
    cotacao = float(input('digite a cotação do dolar atual: '))
    return print(f'\n${dinheiro} em reais equivale a R${dinheiro*cotacao:.2f}\n')

if __name__ == '__main__':
    menu()