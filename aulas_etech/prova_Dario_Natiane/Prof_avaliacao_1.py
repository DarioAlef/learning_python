def read_sales_file(file_name: str) -> list:
    lines = None
    with open(file_name, 'r', encoding='utf-8') as _file:
        lines = _file.readlines()

    product_list = []
    label_list = None

    for index, value in enumerate(lines):
        if index == 0:
            label_list = value.strip('\n').split(',')
            continue

        _values_list = value.strip('\n').split(',')

        product_dict = dict()
        for label, v in zip(label_list, _values_list):
            product_dict[label] = v
        product_list.append(product_dict)

    return product_list


def calculate_total_sales(sales_list: list) -> dict:
    total_sales_by_product = dict()

    for item in sales_list:
        if item.get('Produto') not in total_sales_by_product:
            total_sales_by_product[item.get('Produto')] = 0.0
        total_sales_by_product[item.get('Produto')] += int(item.get('Quantidade')) * float(item.get('Preço'))

    return total_sales_by_product


def generate_report(total_sales: dict):
    print('Sales Report: ')

    for k, v in total_sales.items():
        print(f'{k}: R$ {v:.2f}')


def run():
    sales_list = read_sales_file(file_name='arquivo_vendas.txt')
    # print('sales list -> ', sales_list)
    total_sales = calculate_total_sales(sales_list=sales_list)
    # print('total sales -> ', total_sales)
    generate_report(total_sales=total_sales)


if __name__ == '__main__':
    run()