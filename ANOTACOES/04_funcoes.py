def dividir(a, b):
    quociente = a // b
    resto = a % b
    return quociente, resto

q, r = dividir(13, 5)
print(f'Quociente: {q}, Resto: {r}')

def soma(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado

print(soma(1,2,3,4,5,6,7,8,9,10))
print(soma(10, 20))

def exibir_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

exibir_informacoes(nome='Fulano', sobrenome='Welton', idade=33333)

# """def funcao_qualquer(parâmetro) -> dict """"  isso é uma forma
#de organização do código, no python não interfere na execução do código,
#porém serve para indicar que essa função retorna um dicionário