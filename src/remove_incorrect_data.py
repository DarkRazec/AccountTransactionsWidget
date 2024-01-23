def remove_incorrect_data(data: list[dict]):
    """
    Возвращает список словарей, у которых есть определенный набор ключей
    :param data: исходный список
    :return: список
    """
    return [element for element in data if set(element.keys()).issuperset({'id', 'state', 'date', 'operationAmount', 'description', 'to'})]
