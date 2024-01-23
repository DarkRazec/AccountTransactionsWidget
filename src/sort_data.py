from operator import itemgetter


def sort_data(data: list[dict], reversed=False):
    """
    Возвращает отсортированный список словарей по статусу и дате
    :param data: исходный список
    :param reversed: флаг для вывода списка в обратном порядке
    :return: отсортированный список
    """
    return sorted(data, key=itemgetter('state', 'date'), reverse=reversed)
