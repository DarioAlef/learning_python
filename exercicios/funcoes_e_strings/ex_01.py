#Q.1 - faça uma função que receba uma string como parâmetro e devolva outra string com 
#os carateres embaralhados. Padronize que todos os caracteres serão devolvidos em caixa alta
import random

def embaralha_string(palavra):
    palavra_em_lista = list(palavra)
    
    random.shuffle(palavra_em_lista)
    
    palavra_embaralhada = ''.join(palavra_em_lista) #junta os elementos
    #de uma lista.'' serve para indicar que não haverá elemento separador
    return palavra_embaralhada
    
    
palavra = str(input('\nDigite uma palavra: '))
print(f'\n{embaralha_string(palavra).lower()}\n')