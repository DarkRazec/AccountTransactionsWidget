from operator import itemgetter


def sort_data(data: list[dict], reversed=False):
    return sorted(data, key=itemgetter('state', 'date'), reverse=reversed)
