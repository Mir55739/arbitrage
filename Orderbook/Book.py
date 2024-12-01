import sys
sys.path.insert(0, 'C:/Users/Мир/Documents/Python/Spread')
import bitget.spot.market_api as market
import re
import requests
from binance.client import Client

#bitmart
def calculate_average1(symbol, const):
    URL = f"https://api-cloud.bitmart.com/spot/v1/symbols/book?symbol={symbol}_USDT&depth=10"
    response = requests.get(URL).json()
    ask_bitmart = response['data']['sells']
    bid_bitmart = response['data']['buys']
    volume_in_coins = const/float(ask_bitmart[0]['price'])
    step_usdt = const/(const*10)
    return ask_bitmart, bid_bitmart, volume_in_coins, step_usdt

#mexc
def calculate_average2(symbol, const):
    URL = f"https://api.mexc.com/api/v3/depth?symbol={symbol}USDT&limit=10"
    response = requests.get(URL).json()
    ask_mexc = response['asks']
    bid_mexc = response['bids']
    volume_in_coins = const/float(ask_mexc[0][0])
    step_usdt = const/(const*10)
    return ask_mexc, bid_mexc, volume_in_coins, step_usdt

#binance
def calculate_average3(symbol, const):
    api_key = 'OT4G3dLSVNEa5vXN3RL6BVlMzhDncWvzvFZu5hOF2oGY2qsoWqqz5u2BHIbGapAH'
    api_secret = '32bTDTmCq9S03jM1eYwAlkHmY31UUyeUGWB8CIOfgJ8EgNvgAnTLXCGHSrpkdCr2'
    client = Client(api_key, api_secret)
    ticker_all3 = client.get_order_book(symbol=f"{symbol}USDT", limit='10')
    ask_binance = ticker_all3['asks']
    bid_binance = ticker_all3['bids']
    volume_in_coins = const/float(ask_binance[0][0])
    step_usdt = const/(const*10) 
    return ask_binance, bid_binance, volume_in_coins, step_usdt

#bitget
def calculate_average4(symbol, const):
    api_key = "bg_061cc39012e230776beba6f38e99d851"
    secret_key = "f1d4a202120dd51cf9a4a0bfbbde1c02936d37e0fc1dfc49b064646f6242fc56"
    passphrase = "Tlupov07"  # Password
    marketApi = market.MarketApi(
        api_key, secret_key, passphrase, use_server_time=False, first=False)
    result = marketApi.depth(symbol=f"{symbol}USDT_SPBL", limit='10', type='step0')
    ask_bitget = result['data']['asks']
    bid_bitget = result['data']['bids']   
    volume_in_coins = const/float(ask_bitget[0][0])
    step_usdt = const/(const*10) 
    return ask_bitget, bid_bitget, volume_in_coins, step_usdt






def calculate_average7(symbol, const):
    URL = f"https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol={symbol}-USDT"
    response = requests.get(URL).json()
    ask_kucoin = response['data']['asks']
    bid_kucoin = response['data']['bids']
    #volume_in_coins = const/float(ask_kucoin[0][0])
    step_usdt = const/(const*10)
    # return ask_kucoin, bid_kucoin, volume_in_coins, step_usdt
