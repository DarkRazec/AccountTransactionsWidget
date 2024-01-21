from operator import itemgetter
from src.remove_incorrect_data import remove_incorrect_data


def sort_data(data: list[dict], reversed=False):
    """
    Возвращает отсортированный список словарей по статусу и дате
    :param data: исходный список
    :param reversed: флаг для вывода списка в обратном порядке
    :return: отсортированный список
    """
    return sorted(remove_incorrect_data(data), key=itemgetter('state', 'date'), reverse=reversed)
