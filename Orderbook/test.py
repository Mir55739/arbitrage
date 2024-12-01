from binance.client import Client
api_key = 'OT4G3dLSVNEa5vXN3RL6BVlMzhDncWvzvFZu5hOF2oGY2qsoWqqz5u2BHIbGapAH'
api_secret = '32bTDTmCq9S03jM1eYwAlkHmY31UUyeUGWB8CIOfgJ8EgNvgAnTLXCGHSrpkdCr2'

symbol="BTCUSDT"
const=200
def calculate_average3(symbol, const):
    client = Client(api_key, api_secret)
    ticker_all3 = client.get_order_book(symbol=symbol, limit='10')
    ask_binance = ticker_all3['asks']
    bid_binance = ticker_all3['bids'] 
    print(ask_binance)
    return ticker_all3
calculate_average3(symbol, const)