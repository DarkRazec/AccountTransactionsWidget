from src.sort_data import sort_data
import time


def form_name_num(name: str, num: str):
    """
    Возвращает строку с названием карты или счета и скрытым номером карты или счета
    """
    if name == 'течС':
        return f'{name[::-1]} **{num[3::-1]}'
    return f'{name[::-1]} {num[-1:-5:-1]} {num[-5:-7:-1]}** **** {num[3::-1]}'


def show_operations_data(data: list[dict], num_to_show: int = 5):
    """
    Возвращает строку с данными по последним операциям клиента (по умолчанию количество операций = 5)
    :param data: исходные данные в виде списка с словарями
    :param num_to_show: количество операций
    :return: строку с данными
    """
    data = sort_data(data, reversed=True)
    data_to_show = ""
    for i in range(num_to_show):
        data_time = time.strptime(data[i].get('date').split('T')[0], '%Y-%m-%d')
        data_from = data[i].get('from')
        to_num, to_name = data[i].get('to')[::-1].split(" ", maxsplit=1)

        data_to_show += f"{data_time.tm_mday}.{data_time.tm_mon}.{data_time.tm_year} {data[i].get('description')}\n"
        if data_from:  # эти данные могут отсутствовать, например, при открытии счета
            from_num, from_name = data_from[::-1].split(" ", maxsplit=1)
            data_to_show += f"{form_name_num(from_name, from_num)} -> "
        data_to_show += f"{form_name_num(to_name, to_num)}\n"
        data_to_show += f"{data[i].get('operationAmount').get('amount')} {data[i].get('operationAmount').get('currency').get('name')}\n\n"

    return data_to_show.strip("\n")
