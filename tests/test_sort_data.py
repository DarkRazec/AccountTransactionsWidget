from src.sort_data import sort_data

test_list = [
    {
        "state": "EXECUTED",
        "date": "2018",
    },
    {
        "state": "CANCELED",
        "date": "2019",
    }
]

EXPECTED_LIST = [
    {
        "state": "CANCELED",
        "date": "2019",
    },
    {
        "state": "EXECUTED",
        "date": "2018",
    }
]


def test_sort_data():
    assert sort_data(test_list) == EXPECTED_LIST
    EXPECTED_LIST.reverse()
    assert sort_data(test_list, reversed=True) == EXPECTED_LIST
