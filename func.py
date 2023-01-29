import json
from datetime import date


def open_file(file_json):
    """
    Открывает и обрабаотывает содержимое файла
    :param file_json: файл формата json
    :return: вложенный список со всеми операциями
    """
    with open(file_json, encoding='UTF-8') as file:
        the_data = json.load(file)
        return the_data


def sorted_by_executed_and_date(data_json):
    """
    Сортирует список со всеми операциями и возвращает 5 последних совершенных операций
    :param data_json: вложенный список со всеми операциями
    :return: отсортированный список с пятью последними совершенными операциями
    """
    sorted_list = []
    for i in data_json:
        if i == {}:
            continue
        if i['state'] == "EXECUTED":
            sorted_list.append(i)
    sorted_list.sort(key=lambda dictionary: dictionary['date'], reverse=True)
    return sorted_list[:5]


def formatted_date(transaction_data):
    """
    Приводит дату к нужному виду
    :param transaction_data: библиотека с информацией о транзакции
    :return: дата в подходящем формате
    """
    date_operation = transaction_data.get('date')
    index = date_operation.index('T')
    date_operation = list(map(int, date_operation[0:index].split('-')))
    the_date = date(date_operation[0], date_operation[1], date_operation[2])
    return the_date.strftime("%d.%m.%Y")


def get_description(transaction_data):
    """
    Возвращает описание операции
    :param transaction_data: библиотека с информацией о транзакции
    :return: описание произведенной операции
    """
    description = transaction_data.get('description')
    return description


def get_sender(transaction_data):
    """
    Возвращает информацию о платежной системе и номер счета отправителе"
    :param transaction_data: библиотека с информацией о транзакции
    :return: название платежной системы и номер счета отправителя
    """
    sender = transaction_data.get('from')
    if sender == None:
        return f"Данные об отправителе отсутствуют"
    else:
        sender = sender.split()
        return f"{' '.join(sender[:-1])} {sender[-1][0:2]}** **** {sender[-1][-4:]}"


def get_recipient(transaction_data):
    """
    Возвращает номер счета получателя
    :param transaction_data: библиотека с информацией о транзакции
    :return: номер счета получателя
    """
    resipient = transaction_data.get("to")
    return f"Данные о получателе отсутствуют" if resipient == None else f"{' '.join(resipient.split()[:-1])} **{resipient[-4:]}"


def get_transfer_amount(transaction_data):
    """
    Возвращает сумму перевода
    :param transaction_data: библиотека с информацией о транзакции
    :return: сумма перевода
    """
    transfer_amount = transaction_data['operationAmount'].get("amount")
    return transfer_amount


def get_currency(transaction_data):
    """
    Возвращает валюту совершенной операции
    :param transaction_data: библиотека с информацией о транзакции
    :return: валюта совершенной операции
    """
    currency = transaction_data['operationAmount']['currency'].get('name')
    return currency
