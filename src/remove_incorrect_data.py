def remove_incorrect_data(data: list[dict]):
    """
    Удаляет из списка данные, у которых отсутствует определенный набор ключей
    :param data: исходный список
    :return: список
    """
    for element in data:
        if not set(element.keys()).issuperset({'id', 'state', 'date', 'operationAmount', 'description', 'to'}):
            data.remove(element)
    return data
