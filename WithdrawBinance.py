from binance.client import Client

api_key = 'OT4G3dLSVNEa5vXN3RL6BVlMzhDncWvzvFZu5hOF2oGY2qsoWqqz5u2BHIbGapAH'
api_secret = '32bTDTmCq9S03jM1eYwAlkHmY31UUyeUGWB8CIOfgJ8EgNvgAnTLXCGHSrpkdCr2'


def convert_symbol(symbol):
    return f"{symbol}_USDT"


def get_withdrawal_info():
    client = Client(api_key, api_secret)
    asset_details = client.get_asset_details()
    withdrawal_info = {}
    for asset, details in asset_details.items():
        name = asset
        withdraw_fee = details['withdrawFee']
        withdrawal_info[name] = (withdraw_fee)
    return withdrawal_info


get_withdrawal_info()
