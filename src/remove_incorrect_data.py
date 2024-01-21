def remove_incorrect_data(data: list[dict]):
    # incorrect_data = []  #data = sorted(data, key=itemgetter('state', 'date')) #data[0].keys()
    for element in data:
        if element.keys() != ('id', 'state', 'date', 'operationAmount', 'description', 'from', 'to'):
            data.remove(element)
    return data
