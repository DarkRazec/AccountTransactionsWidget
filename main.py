from json import load
from src.remove_incorrect_data import remove_incorrect_data
from src.sort_data import sort_data

with open("data/operations.json", encoding="utf8") as f:
    data = load(f)

data = sort_data(remove_incorrect_data(data), reversed=True)
for i in range(5):
    print(data[i].get('date'), data[i].get('description'))
    if 'крытие' in data[i].get('description'):
        print(data[i].get('to'))
    else:
        print(data[i].get('from'), data[i].get('to'))
    print(data[i].get('operationAmount').get('amount'), data[i].get('operationAmount').get('currency').get('name'), '\n')
