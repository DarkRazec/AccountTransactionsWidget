from src.show_operations_data import show_operations_data

test_list = [
    {
        "id": 596171168,
        "state": "EXECUTED",
        "date": "2018-07-11T02:26:18.671407",
        "operationAmount": {
            "amount": "79931.03",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 72082042523231456215"
    },
    {},
    {
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {
            "amount": "40701.91",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Gold 5999414228426353",
        "to": "Счет 72731966109147704472"
    }
]

EXPECTED_STR = '''11.7.2018 Открытие вклада
Счет **6215
79931.03 руб.

4.4.2018 Перевод организации
Visa Gold 5999 41** **** 6353 -> Счет **4472
40701.91 USD'''


def test_show_op_data():
    assert show_operations_data(test_list, 2) == EXPECTED_STR
