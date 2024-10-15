#leia o arquivo usuarios.txt e imprim as informações conforme o exemplo abaixo:

# --------------------- Info Usuários ---------------------
# Nr:1 | Usuário: alexandre | 
# Espaço utilizado: 434,99 MB | % do uso : 16,85%
# ---------------------------------------------------------


# obtendo linhas do arquivo e colocando-as em uma lista.
def _read_file_to_list():
    lines = None
    with open('usuarios.txt', 'r', encoding='utf-8') as _file:
        lines = _file.readlines()
    return lines


def _list_to_list_dict_user(lines_file: list):
    list_user = []
    list_labels = ['NR', 'Usuário', 'Espaço Utilizado', 'Porcentagem de Uso']

    for index, value in enumerate(lines_file): 
        if index == 0:              #laço para dividir a lista de linhas
            continue                #em lista itens, usando ';' para identidicar
        _values = value.split(';')

        user_dict = dict()   #adiciona cada par chave valor ao user_dict           
        for label, v in zip(list_labels, _values):
            user_dict[label] = v
        list_user.append(user_dict)

    return list_user


def _show_info(user_dict: list):
    pass


if __name__ == '__main__':
    # obter linhas do arquivo
    lines_file = _read_file_to_list()
    print(lines_file)
    dict_user = _list_to_list_dict_user(lines_file=lines_file)
    print(dict_user)
    
for i in dict_user:
    print('---------------- info',i['Usuário'],'-----------------')
    print(i['NR'],' | Usuário:', i['Usuário'],'|')
    print('Espaço Utilizado: ',i['Espaço Utilizado'],'| % do uso: ',i['Porcentagem de Uso'])
    print('------------------------------------------------\n\n')
    # print(i)