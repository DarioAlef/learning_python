#leia o arquivo usuarios.txt e imprim as informações conforme o exemplo abaixo:

# --------------------- Info Usuários ---------------------
# Nr:1 | Usuário: alexandre | 
# Espaço utilizado: 434,99 MB | % do uso : 16,85%
# ---------------------------------------------------------

def ler_arquivo():
#lê o txt e transforma e transforma em lista, cada item é uma linha
    with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()  
    return linhas   #método .readlines() transforma cada linha em um item de uma lista

def lista_para_dicionario(linhas):
    lista_usuarios = []
    lista_cabecalho = ['NR', 'Usuário', 'Espaço Utilizado', 'Porcentagem de Uso']
    
    for indice, itens in enumerate(linhas): #enumerar a lista linhas
        if indice == 0:
            continue   #pula o linha que tem os cabeçalhos
        itens2 = itens.split(';')
#cada linha da lista 'linhas' será atribuída às variáveis 'indice' e 'itens'
#'itens2' irá dividir cada string em substring usando ';' como ponto de divisão

        dicionario_usuarios = dict()
        for cabecalho, v in zip(lista_cabecalho, itens2): 
#a cada laço, será executado um sub laço, onde irá juntar o cabecalho 'lista_cabecalho'
#com os itens da substring 'itens2'. Ou seja, da lista de linhas, cada pedaço será
#separado e juntado com os itens do cabecalho
            dicionario_usuarios[cabecalho] = v
        lista_usuarios.append(dicionario_usuarios)
    
    return lista_usuarios


if __name__ == '__main__':
    linhas_arquivo = ler_arquivo()
    print(linhas_arquivo)
    usuario_dicionario = lista_para_dicionario(linhas=linhas_arquivo)
    print(usuario_dicionario)
    
for i in usuario_dicionario:
    print('---------------- info',i['Usuário'],'-----------------')
    print(i['NR'],' | Usuário:', i['Usuário'],'|')
    print('Espaço Utilizado: ',i['Espaço Utilizado'],'| % do uso: ',i['Porcentagem de Uso'])
    print('------------------------------------------------\n\n')