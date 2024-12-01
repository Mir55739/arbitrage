import requests
import re
from WithdrawKucoin import get_withdrawals
#from Orderbook.Kucoinbook import calculate_average_price7, calculate_average7
from common import const


def get_ticker_data7():
    bitmart = requests.get('https://api.kucoin.com/api/v1/market/allTickers')
    ticker_data7 = bitmart.json()
    return ticker_data7


def get_prices_kucoin(ticker_data7):
    ticker_all = ticker_data7['data']['ticker']
    ask_prices_kucoin = {ticker['symbol']: float(
        ticker['sell']) for ticker in ticker_all if ticker['sell'] is not None}
    bid_prices_kucoin = {ticker['symbol']: float(
        ticker['buy']) for ticker in ticker_all if ticker['buy'] is not None}
# Без "_"
    ask_prices_kucoin1 = {symbol.replace(
        "-", ""): price for symbol, price in ask_prices_kucoin.items()}
    bid_prices_kucoin1 = {symbol.replace(
        "-", ""): price for symbol, price in bid_prices_kucoin.items()}
    return ask_prices_kucoin, bid_prices_kucoin, ask_prices_kucoin1, bid_prices_kucoin1

# Bitmart


def send_profit71_messages(update, common_symbols71, ask_prices_kucoin1, bid_prices_bitmart1):
    # Создание списка кортежей (символ, профит2)
    profits3 = []
    for symbol in common_symbols71:
        if symbol in ask_prices_kucoin1:
            if ask_prices_kucoin1[symbol] == 0:
                profit3 = 0
            else:
                profit3 = (
                    bid_prices_bitmart1[symbol] - ask_prices_kucoin1[symbol]) / ask_prices_kucoin1[symbol] * 100
        else:
            profit3 = 0
        profits3.append((symbol, profit3))
        # Сортировка списка по профиту в порядке убывания
    profits3.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке

    for symbol, profit3 in profits3:
        if 0.5 <= profit3 <= 20:
            symbol1 = symbol.replace(
                "USDT", "-USDT")
            symbol2 = symbol.replace(
                "USDT", "_USDT")
            kucoin_url = f"https://www.kucoin.com/ru/trade/{symbol1}"
            bitmart_url = f"https://www.bitmart.com/trade/ru-RU?layout=basic&theme=dark&symbol={symbol2}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            withdrawals = get_withdrawals(base_symbol)
            volume_in_coins = const/float(ask_prices_kucoin1[symbol])
            step_usdt = const/(const*10)

            text = f"{symbol}\n<a href='{kucoin_url}'>Покупка</a> на Kucoin = {ask_prices_kucoin1[symbol]}\n<a href='{bitmart_url}'>Продажа</a> на Bitmart = {bid_prices_bitmart1[symbol]}\nСпред: {profit3:.2f}%"
            for withdrawal in withdrawals:
                chain = withdrawal["chain"]
                status = withdrawal["status"]
                fee = withdrawal['fee']
                fee = float(fee) * float(ask_prices_kucoin1[symbol])
                text += f"\nСеть вывода: {chain}\nСтатус вывода: {status}\nРазмер комиссии: {fee:.2f}"
            # best_ask_volume, best_ask_price, best_ask_orders, best_bid_volume, best_bid_price, best_bid_orders, best_profit = calculate_average_price7(
             #   symbol, volume_in_coins, step_usdt)
            #text += f"\nЛучший вариант: покупка {best_ask_volume:.2f} USDT по средней цене {best_ask_price:.6f} ({best_ask_orders} ордеров) и продажа {best_bid_volume:.2f} USDT по средней цене {best_bid_price:.6f} ({best_bid_orders} ордеров). Прибыль: {best_profit:.2f} USDT"
            update.message.reply_html(
                text, disable_web_page_preview=True)

# Mexc


def send_profit72_messages(update, common_symbols72, ask_prices_kucoin1, bid_prices_mexc1):
    # Создание списка кортежей (символ, профит2)
    profits3 = []
    for symbol in common_symbols72:
        if symbol in ask_prices_kucoin1:
            if ask_prices_kucoin1[symbol] == 0:
                profit3 = 0
            else:
                profit3 = (
                    bid_prices_mexc1[symbol] - ask_prices_kucoin1[symbol]) / ask_prices_kucoin1[symbol] * 100
        else:
            profit3 = 0
        profits3.append((symbol, profit3))
        # Сортировка списка по профиту в порядке убывания
    profits3.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке

    for symbol, profit3 in profits3:
        if 0.5 <= profit3 <= 20:
            symbol1 = symbol.replace(
                "USDT", "-USDT")
            symbol2 = symbol.replace(
                "USDT", "_USDT")
            kucoin_url = f"https://www.kucoin.com/ru/trade/{symbol1}"
            mexc_url = f"https://www.mexc.com/ru-RU/exchange/{symbol2}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            withdrawals = get_withdrawals(base_symbol)
            text = f"{symbol}\n<a href='{kucoin_url}'>Покупка</a> на Kucoin = {ask_prices_kucoin1[symbol]}\n<a href='{mexc_url}'>Продажа</a> на Mexc = {bid_prices_mexc1[symbol]}\nСпред: {profit3:.2f}%"
            for withdrawal in withdrawals:
                chain = withdrawal["chain"]
                status = withdrawal["status"]
                fee = withdrawal['fee']
                fee = float(fee) * float(ask_prices_kucoin1[symbol])
                text += f"\nСеть вывода: {chain}\nСтатус вывода: {status}\nРазмер комиссии: {fee:.2f}"

            update.message.reply_html(
                text, disable_web_page_preview=True)

# Binance


def send_profit73_messages(update, common_symbols73, ask_prices_kucoin1, bid_prices_binance):
    # Создание списка кортежей (символ, профит2)
    profits3 = []
    for symbol in common_symbols73:
        if symbol in ask_prices_kucoin1:
            if ask_prices_kucoin1[symbol] == 0:
                profit3 = 0
            else:
                profit3 = (
                    bid_prices_binance[symbol] - ask_prices_kucoin1[symbol]) / ask_prices_kucoin1[symbol] * 100
        else:
            profit3 = 0
        profits3.append((symbol, profit3))
        # Сортировка списка по профиту в порядке убывания
    profits3.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке

    for symbol, profit3 in profits3:
        if 0.5 <= profit3 <= 20:
            symbol1 = symbol.replace(
                "USDT", "-USDT")
            symbol2 = symbol.replace(
                "USDT", "_USDT")
            kucoin_url = f"https://www.kucoin.com/ru/trade/{symbol1}"
            binance_url = f"https://www.binance.com/ru/trade/{symbol2}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            withdrawals = get_withdrawals(base_symbol)
            text = f"{symbol}\n<a href='{kucoin_url}'>Покупка</a> на Kucoin = {ask_prices_kucoin1[symbol]}\n<a href='{binance_url}'>Продажа</a> на Binance = {bid_prices_binance[symbol]}\nСпред: {profit3:.2f}%"
            for withdrawal in withdrawals:
                chain = withdrawal["chain"]
                status = withdrawal["status"]
                fee = withdrawal['fee']
                fee = float(fee) * float(ask_prices_kucoin1[symbol])
                text += f"\nСеть вывода: {chain}\nСтатус вывода: {status}\nРазмер комиссии: {fee:.2f}"

            update.message.reply_html(
                text, disable_web_page_preview=True)

# Bitget


def send_profit74_messages(update, common_symbols74, ask_prices_kucoin1, bid_prices_bitget):
    # Создание списка кортежей (символ, профит2)
    profits3 = []
    for symbol in common_symbols74:
        if symbol in ask_prices_kucoin1:
            if ask_prices_kucoin1[symbol] == 0:
                profit3 = 0
            else:
                profit3 = (
                    bid_prices_bitget[symbol] - ask_prices_kucoin1[symbol]) / ask_prices_kucoin1[symbol] * 100
        else:
            profit3 = 0
        profits3.append((symbol, profit3))
        # Сортировка списка по профиту в порядке убывания
    profits3.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке

    for symbol, profit3 in profits3:
        if 0.5 <= profit3 <= 20:
            symbol1 = symbol.replace(
                "USDT", "-USDT")
            symbol2 = symbol.replace(
                "USDT", "_USDT")
            kucoin_url = f"https://www.kucoin.com/ru/trade/{symbol1}"
            bitget_url = f"https://www.bitget.com/ru/spot/{symbol}_SPBL?type=spot"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            withdrawals = get_withdrawals(base_symbol)
            text = f"{symbol}\n<a href='{kucoin_url}'>Покупка</a> на Kucoin = {ask_prices_kucoin1[symbol]}\n<a href='{bitget_url}'>Продажа</a> на Bitget = {bid_prices_bitget[symbol]}\nСпред: {profit3:.2f}%"
            for withdrawal in withdrawals:
                chain = withdrawal["chain"]
                status = withdrawal["status"]
                fee = withdrawal['fee']
                fee = float(fee) * float(ask_prices_kucoin1[symbol])
                text += f"\nСеть вывода: {chain}\nСтатус вывода: {status}\nРазмер комиссии: {fee:.2f}"

            update.message.reply_html(
                text, disable_web_page_preview=True)

# Gate


def send_profit75_messages(update, common_symbols75, ask_prices_kucoin1, bid_prices_gate1):
    # Создание списка кортежей (символ, профит2)
    profits3 = []
    for symbol in common_symbols75:
        if symbol in ask_prices_kucoin1:
            if ask_prices_kucoin1[symbol] == 0 or not ask_prices_kucoin1[symbol] or not bid_prices_gate1[symbol]:
                profit3 = 0
            else:
                profit3 = (
                    bid_prices_gate1[symbol] - ask_prices_kucoin1[symbol]) / ask_prices_kucoin1[symbol] * 100
        else:
            profit3 = 0
        profits3.append((symbol, profit3))
        # Сортировка списка по профиту в порядке убывания
    profits3.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке

    for symbol, profit3 in profits3:
        if 0.5 <= profit3 <= 20:
            symbol1 = symbol.replace(
                "USDT", "-USDT")
            symbol2 = symbol.replace(
                "USDT", "_USDT")
            kucoin_url = f"https://www.kucoin.com/ru/trade/{symbol1}"
            gate_url = f"https://www.gate.io/ru/trade/{symbol2}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            withdrawals = get_withdrawals(base_symbol)
            text = f"{symbol}\n<a href='{kucoin_url}'>Покупка</a> на Kucoin = {ask_prices_kucoin1[symbol]}\n<a href='{gate_url}'>Продажа</a> на Gate = {bid_prices_gate1[symbol]}\nСпред: {profit3:.2f}%"
            for withdrawal in withdrawals:
                chain = withdrawal["chain"]
                status = withdrawal["status"]
                fee = withdrawal['fee']
                fee = float(fee) * float(ask_prices_kucoin1[symbol])
                text += f"\nСеть вывода: {chain}\nСтатус вывода: {status}\nРазмер комиссии: {fee:.2f}"

            update.message.reply_html(
                text, disable_web_page_preview=True)

# Huobi


def send_profit76_messages(update, common_symbols76, ask_prices_kucoin1, bid_prices_huobi):
    # Создание списка кортежей (символ, профит2)
    profits3 = []
    for symbol in common_symbols76:
        if symbol in ask_prices_kucoin1:
            if ask_prices_kucoin1[symbol] == 0:
                profit3 = 0
            else:
                profit3 = (
                    bid_prices_huobi[symbol] - ask_prices_kucoin1[symbol]) / ask_prices_kucoin1[symbol] * 100
        else:
            profit3 = 0
        profits3.append((symbol, profit3))
        # Сортировка списка по профиту в порядке убывания
    profits3.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке

    for symbol, profit3 in profits3:
        if 0.5 <= profit3 <= 20:
            symbol1 = symbol.replace(
                "USDT", "-USDT")
            symbol2 = symbol.replace(
                "USDT", "_USDT")
            kucoin_url = f"https://www.kucoin.com/ru/trade/{symbol1}"
            hyuobi_url = f"https://www.huobi.com/ru-ru/trade/{symbol2}?type=spot"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            withdrawals = get_withdrawals(base_symbol)
            text = f"{symbol}\n<a href='{kucoin_url}'>Покупка</a> на Kucoin = {ask_prices_kucoin1[symbol]}\n<a href='{hyuobi_url}'>Продажа</a> на Huobi = {bid_prices_huobi[symbol]}\nСпред: {profit3:.2f}%"
            for withdrawal in withdrawals:
                chain = withdrawal["chain"]
                status = withdrawal["status"]
                fee = withdrawal['fee']
                fee = float(fee) * float(ask_prices_kucoin1[symbol])
                text += f"\nСеть вывода: {chain}\nСтатус вывода: {status}\nРазмер комиссии: {fee:.2f}"

            update.message.reply_html(
                text, disable_web_page_preview=True)
