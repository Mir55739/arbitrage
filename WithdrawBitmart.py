from BitmartSDK.bitmart.cloud_log import CloudLog
from BitmartSDK.bitmart.api_account import APIAccount
import time
import json

CloudLog.set_logger_level('info')


def get_withdraw_fees(api_key, secret_key, memo):
    contracAPI = APIAccount(api_key, secret_key, memo, timeout=(3, 10))
    r = contracAPI.get_currencies()
    body = r[0]
    currencies = body['data']['currencies']
    print(currencies)
    withdraw_fees = []
    for currency in currencies:
        if currency['withdraw_enabled']:
            try:
                r = contracAPI.get_withdraw_charge(currency['currency'])
                body = r[0]
                withdraw_fee = body['data']['withdraw_fee']
                withdraw_fees.append((currency['currency'], withdraw_fee))
            except Exception as e:
                print(
                    f"Ошибка при получении информации о валюте {currency['currency']}: {e}")

            # Добавляем задержку между запросами
            time.sleep(0.5)

    return withdraw_fees


def save_withdraw_fees(withdraw_fees, filename):
    # Преобразование списка кортежей в словарь
    withdraw_fees_dict = dict(withdraw_fees)

    # Сериализация словаря в строку JSON
    json_str = json.dumps(withdraw_fees_dict, indent=4)

    # Запись строки JSON в текстовый файл
    with open(filename, 'w') as f:
        f.write(json_str)


api_key = "e2ce0607ec00afed2176c7e8e9eb6b25d4fd921b"
secret_key = "a8ba97b8fd1cb5393a25812fefa82c0171871474d9dbdae5e6e5bc573421e5b2"
memo = "Your Memo"

withdraw_fees = get_withdraw_fees(api_key, secret_key, memo)

# Сохранение комиссий за вывод в текстовый файл
save_withdraw_fees(withdraw_fees, 'withdraw_fees.txt')
