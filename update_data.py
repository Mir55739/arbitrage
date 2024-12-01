from Mexc import get_ticker_data2, get_prices_mexc
from BitMart import get_ticker_data, get_prices_bitmart
from Binance import get_ticker_data3, get_prices_binance
from Bitget import get_ticker_data43, get_prices_bitget
from Gate import get_ticker_data5, get_prices_gate
from Huobi.Huobi import get_ticker_data6, get_prices_huobi


def update_data(context):
    ticker_data = get_ticker_data()
    ticker_data2 = get_ticker_data2()
    ticker_data3 = get_ticker_data3()
    ticker_data43 = get_ticker_data43()
    ticker_data5 = get_ticker_data5()
    ticker_data6 = get_ticker_data6()
 ##########################################
    ask_prices_bitmart, bid_prices_bitmart, ask_prices_bitmart1, bid_prices_bitmart1 = get_prices_bitmart(
        ticker_data)
    ask_prices_mexc, bid_prices_mexc, ask_prices_mexc1, bid_prices_mexc1 = get_prices_mexc(
        ticker_data2)
    ask_prices_binance, bid_prices_binance = get_prices_binance(
        ticker_data3)
    ask_prices_bitget, bid_prices_bitget = get_prices_bitget(ticker_data43)
    ask_prices_gate, bid_prices_gate, ask_prices_gate1, bid_prices_gate1 = get_prices_gate(
        ticker_data5)
    ask_prices_huobi, bid_prices_huobi = get_prices_huobi(ticker_data6)
