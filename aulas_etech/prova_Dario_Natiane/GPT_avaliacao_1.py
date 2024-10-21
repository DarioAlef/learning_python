def ler_arquivo_vendas(nome_arquivo):
    list_vendas = []
    list_labels = ['Produto', 'Quantidade', 'Preço']

    with open('vendas.txt', 'r', encoding='utf-8') as _file:
        lines_file = _file.readlines()

    for index, linha in enumerate(lines_file):
        if index == 0:
            continue
        valores = linha.strip().split(',')

        vendas = dict()
        for label, v in zip(list_labels, valores):
            if label == 'Quantidade':
                vendas[label] = int(v)
            elif label == 'Preço':
                vendas[label] = float(v)
            else:
                vendas[label] = v
        list_vendas.append(vendas)

    return list_vendas


def calcular_total_vendas(lista_vendas):
    total_vendas = {}

    for venda in lista_vendas:
        produto = venda['Produto']
        quantidade = venda['Quantidade']
        preco = venda['Preço']

        total = quantidade * preco

        if produto in total_vendas:
            total_vendas[produto] += total
        else:
            total_vendas[produto] = total

    return total_vendas


def gerar_relatorio(total_vendas):
    print("Relatório de Vendas:\n")
    for produto, total in total_vendas.items():
        print(f"{produto}: R$ {total:.2f}")


def executar():
    nome_arquivo = 'arquivo_vendas.txt'
    vendas = ler_arquivo_vendas(nome_arquivo)
    print(f'\n{vendas}\n\n')
    totais = calcular_total_vendas(vendas)
    print(totais,'\n\n')
    gerar_relatorio(totais)


if __name__ == '__main__':
    executar()