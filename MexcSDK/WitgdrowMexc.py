import requests
import hashlib
import hmac
import time


api_key = "mx0vgldyoifWSHZ9AL"
secret_key = "8af018026aff45b8800fad33158b8507"
url = "https://api.mexc.com/api/v3/capital/config/getall"


def convert_symbol(symbol):
    return f"{symbol}_USDT"


def get_withdrawal_info():
    # получаем текущую метку времени в миллисекундах
    timestamp = int(time.time() * 1000)

    params = {
        'api_key': api_key,
        'timestamp': timestamp,
    }

    # создаем строку параметров запроса
    param_string = "&".join(f"{k}={v}" for k, v in sorted(params.items()))

    # генерируем подпись с использованием секретного ключа
    signature = hmac.new(secret_key.encode(),
                         param_string.encode(), hashlib.sha256).hexdigest()

    # добавляем подпись в параметры запроса
    params['signature'] = signature

    # отправляем GET запрос на сервер MXC
    response = requests.get(url, params=params)
    data = response.json()
    withdrawal_info = {}
    print(data)
    for token in data:
        name = token['coin']
        #name = convert_symbol(name)
        networks = token['networkList']
        for network in networks:
            network_name = network['network']
            withdraw = network['withdrawEnable']
            fee = network['withdrawFee']
            withdrawal_info[name] = (network_name, withdraw, fee)
    return withdrawal_info


get_withdrawal_info()
