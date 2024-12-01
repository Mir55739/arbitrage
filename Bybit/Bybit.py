from pybit.unified_trading import HTTP

def get_ticker_data8():
    session = HTTP(testnet=True)
    ticker_data8 = session.get_tickers(
    category="spot",
    )
    return ticker_data8
ticker_data8= get_ticker_data8()

def get_prices_bybit(ticker_data8):
    ticker_all = ticker_data8['result']['list']
    ask_prices_bybit = {ticker['symbol']: float(
        ticker['ask1Price']) for ticker in ticker_all if ticker['ask1Price']}
    bid_prices_bybit = {ticker['symbol']: float(
        ticker['bid1Price']) for ticker in ticker_all if ticker['bid1Price']}
    return ask_prices_bybit, bid_prices_bybit
get_prices_bybit(ticker_data8)