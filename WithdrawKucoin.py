import time
import requests
import hmac
import base64
import hashlib
symbol = "USDT"


def get_withdrawals(symbol: str):
    api_key = "6480e0d046287b0001ad6d08"
    api_secret = "31ca2824-4d70-4bd5-919f-c88c88540891"
    api_passphrase = "Tlupov07"

    headers = {
        'KC-API-KEY': api_key,
        'KC-API-SECRET': api_secret
    }

    response = requests.get(
        f'https://openapi-v2.kucoin.com/api/v2/currencies/{symbol}', headers=headers)
    data = response.json()

    withdrawals = []
    for item in data["data"]['chains']:
        chain = item['chain']
        status = item['isWithdrawEnabled']
        fee = item['withdrawalMinFee']
        withdrawals.append({"chain": chain, "status": status, "fee": fee})
    return withdrawals


get_withdrawals(symbol)
