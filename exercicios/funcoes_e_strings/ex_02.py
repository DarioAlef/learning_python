#Q.02 -  Faça uma função que retorne o reverso de um número inteiro informado


def reverso(num):
#é necessário passar para string pois o método :: é apenas para strings
    num_string = str(num)
    num2 = num_string[::-1] #os dois pontos indicam que está ocorrendo
#um slice, e poderímos colocar um índice. O segundo dois pontos indica que
#será a string inteira e o -1 indica que será de trás para frente. ou seja
#inverter a string de trás pra frente
    inteiro_num = int(num2)
    
    return inteiro_num
    
    
num = int(input('Digite um número: '))
print(f'\nO número invertido é: {reverso(num)}')