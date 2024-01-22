import pytest

from src.remove_incorrect_data import remove_incorrect_data

test_list = [
    {
        'id': 1,
        'state': 2,
        'date': 3,
        'operationAmount': 4,
        'description': 5,
        'to': 7
    },
    {
        'id': 1,
        'state': 2,
        'date': 3
    }
]
test_list_2 = [
    {
        'id': 1,
        'state': 2,
        'date': 3,
        'operationAmount': 4,
        'description': 5,
        'from': 6,
        'to': 7
    }
]

test_list_3 = [{'id': 1}]

KEYS = {'id', 'state', 'date', 'operationAmount', 'description', 'to'}


@pytest.mark.parametrize('test_lists, keys', [
    ([True if set(element.keys()).issuperset(KEYS) else False for element in remove_incorrect_data(test_list)], KEYS),
    ([True if set(element.keys()).issuperset(KEYS) else False for element in remove_incorrect_data(test_list_2)], KEYS),
])
def test_rm_inc_data(test_lists, keys):
    assert test_lists.count(True) == len(test_lists)
