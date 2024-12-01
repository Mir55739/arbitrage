
import gate_api
from gate_api.exceptions import ApiException

# Установите свой API ключ и секрет
api_key = "d231a4c7b1cff64ec9edb237173705e4"
api_secret = "0cae023f4d7317a57d72d4c3fb24cde914a581381cb5f16b27a09c200d7e6678"

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
