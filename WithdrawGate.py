
import gate_api
from gate_api.exceptions import ApiException

# Установите свой API ключ и секрет
api_key = "ec9688e679495a32827b8821f0edaa47"
api_secret = "552c686a4bf9b130dd42e782495091b3b7327be686ac7e3ce87a2f0ebd305c08"

# Установите валюту
currency = "USDT"

# Создайте объект конфигурации и установите API ключ и секрет
config = gate_api.Configuration()
config.key = api_key
config.secret = api_secret

# Создайте экземпляр клиента API Gate.io
client = gate_api.WalletApi(gate_api.ApiClient(config))

try:
    # Получите список записей о выводе средств для указанной валюты
    withdrawals = client.list_withdrawals(currency=currency)
    for withdrawal in withdrawals:
        print(
            f"ID: {withdrawal['id']}, Валюта: {withdrawal['currency']}, Сумма: {withdrawal['amount']}, Адрес: {withdrawal['address']}")
except ApiException as e:
    print(f"Произошла ошибка: {e}")
