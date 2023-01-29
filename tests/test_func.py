from func import *



def test_open_file():
    assert open_file('test_open_file.json') == [{'id': 441945886, 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, {'id': 41428829, 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}]


def test_formatted_date():
    assert formatted_date({'date': '2018-06-30T02:08:58.425572'}) == "30.06.2018"


def test_get_description():
    assert get_description({"description": "Перевод организации"}) == "Перевод организации"


def test_get_sender():
    assert get_sender({"from": "MasterCard 7158300734726758"}) == "MasterCard 71** **** 6758"
    assert get_sender({'1': 1}) == "Данные об отправителе отсутствуют"


def test_get_recipient():
    assert get_recipient({"to": "Счет 35383033474447895560"}) == "Счет **5560"
    assert get_recipient({"1": 1}) == "Данные о получателе отсутствуют"


def test_get_transfer_amount():
    assert get_transfer_amount({"operationAmount": {"amount": "9824.07"}}) == "9824.07"


def test_get_currency():
    assert get_currency({"operationAmount": {"currency": {"name": "USD"}}}) == "USD"
