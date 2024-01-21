def remove_incorrect_data(data: list[dict]):
    """
    Удаляет данные с ошибками из списка
    :param data: исходный список
    :return: список
    """
    for element in data:
        if element.keys() != ('id', 'state', 'date', 'operationAmount', 'description', 'from', 'to'):
            data.remove(element)
    return data
