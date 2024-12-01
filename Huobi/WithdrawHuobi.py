# huobi_api.py
import requests


def get_withdrawal_fees(currency):
    currency = currency.lower()
    url = f"https://api.huobi.pro/v2/reference/currencies?currency={currency}"
    response = requests.get(url)
    fees = {}
    if response.status_code == 200:
        data = response.json()
        chains = data["data"][0]["chains"]
        for chain in chains:
            chain_name = chain["displayName"]
            if "transactFeeWithdraw" in chain:
                fees[chain_name] = {"type": "fixed",
                                    "fee": chain["transactFeeWithdraw"]}
            elif "transactFeeRateWithdraw" in chain:
                fees[chain_name] = {"type": "rate",
                                    "fee": chain["transactFeeRateWithdraw"]}
            else:
                fees[chain_name] = {"type": "unknown", "fee": None}
    return fees
