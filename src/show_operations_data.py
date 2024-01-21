
from src.sort_data import sort_data


def show_operations_data(data: list[dict], num_to_show: int = 5):
    """
    Возвращает строку с данными по последним операциям клиента (по умолчанию количество операций = 5)
    :param data: исходные данные
    :param num_to_show: количество операций для вывода
    :return: строку с данными
    """
    data = sort_data(data, reversed=True)
    data_to_show = ""
    for i in range(num_to_show):
        data_descr = data[i].get('description')
        data_to_show += f"{data[i].get('date')}, {data_descr}\n"
        if 'крытие' in data_descr:
            data_to_show += f"{data[i].get('to')}\n"
        else:
            data_to_show += f"{data[i].get('from')} -> {data[i].get('to')}\n"
        data_to_show += f"{data[i].get('operationAmount').get('amount')}, {data[i].get('operationAmount').get('currency').get('name')}\n\n"
    return data_to_show.strip("\n")
