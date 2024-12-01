from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
gate_buy_enabled = True
gate_sell_enabled = True

configuration = gate_api.Configuration(
    host="https://api.gateio.ws/api/v4"
)


def get_ticker_data5():
    api_client = gate_api.ApiClient(configuration)
    # Create an instance of the API class
    api_instance = gate_api.SpotApi(api_client)
    timezone = 'utc0'
    # Retrieve ticker information
    ticker_data5 = api_instance.list_tickers(timezone=timezone)
    return ticker_data5


def get_prices_gate(ticker_data5):
    ticker_all2 = ticker_data5
    ask_prices_gate = {ticker.currency_pair:
                       ticker.lowest_ask for ticker in ticker_all2}
    bid_prices_gate = {ticker.currency_pair:
                       ticker.highest_bid for ticker in ticker_all2}
    for key in ask_prices_gate:
        if ask_prices_gate[key]:
            ask_prices_gate[key] = float(ask_prices_gate[key])
        else:
            # Пропуск пустой строки
            continue
    for key in bid_prices_gate:
        if bid_prices_gate[key]:
            bid_prices_gate[key] = float(bid_prices_gate[key])
        else:
            # Пропуск пустой строки
            continue
    ask_prices_gate1 = {symbol.replace(
        "_", ""): price for symbol, price in ask_prices_gate.items()}
    bid_prices_gate1 = {symbol.replace(
        "_", ""): price for symbol, price in bid_prices_gate.items()}
    return ask_prices_gate, bid_prices_gate, ask_prices_gate1, bid_prices_gate1

# //////////////////////////////////////////////////////

# Bitmart


def send_profit51_messages(update, common_symbols51, ask_prices_gate, bid_prices_bitmart):
    #withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits2 = []
    for symbol in common_symbols51:
        if ask_prices_gate[symbol] == 0:
            profit2 = 0
        else:
            if ask_prices_gate[symbol]:
                profit2 = (bid_prices_bitmart[symbol] - float(
                    ask_prices_gate[symbol])) / float(ask_prices_gate[symbol]) * 100
            else:
                # Обработка пустой строки
                continue
        profits2.append((symbol, profit2))

    # Сортировка списка по профиту в порядке убывания
    profits2.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit2 in profits2:
        if 0.5 <= profit2 <= 20:
            gate_url = f"https://www.gate.io/ru/trade/{symbol}"
            bitmart_url = f"https://www.bitmart.com/trade/ru-RU?layout=basic&theme=dark&symbol={symbol}"
            symbol1 = symbol
            symbol = symbol.split("_USDT")[0]
            #network_name, withdraw, fee = withdrawal_info[symbol]
            #fee = float(fee) * ask_prices_gate[symbol1]
            text = f"{symbol1}\n<a href='{gate_url}'>Покупка</a> на Gate = {ask_prices_gate[symbol1]}\n<a href='{bitmart_url}'>Продажа</a> на Bitmart = {bid_prices_bitmart[symbol1]}\nСпред: {profit2:.2f}%"
            update.message.reply_html(text, disable_web_page_preview=True)

           # \nСеть вывода: {network_name}\nСтатус вывода: {withdraw}\nРазмер комиссии: {fee:.2f}

# Mexc


def send_profit52_messages(update, common_symbols52, ask_prices_gate, bid_prices_mexc):
    #withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits52 = []
    for symbol in common_symbols52:
        if ask_prices_gate[symbol] == 0:
            profit52 = 0
        else:
            if ask_prices_gate[symbol]:
                profit52 = (bid_prices_mexc[symbol] - float(
                    ask_prices_gate[symbol])) / float(ask_prices_gate[symbol]) * 100
            else:
                # Обработка пустой строки
                continue
        profits52.append((symbol, profit52))

    # Сортировка списка по профиту в порядке убывания
    profits52.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit52 in profits52:
        if 0.5 <= profit52 <= 20:
            gate_url = f"https://www.gate.io/ru/trade/{symbol}"
            mexc_url = f"https://www.mexc.com/ru-RU/exchange/{symbol}"
            symbol1 = symbol
            symbol = symbol.split("_USDT")[0]
            #network_name, withdraw, fee = withdrawal_info[symbol]
            #fee = float(fee) * ask_prices_gate[symbol1]
            text = f"{symbol1}\n<a href='{gate_url}'>Покупка</a> на Gate = {ask_prices_gate[symbol1]}\n<a href='{mexc_url}'>Продажа</a> на Mexc = {bid_prices_mexc[symbol1]}\nСпред: {profit52:.2f}%"
            update.message.reply_html(text, disable_web_page_preview=True)

           # \nСеть вывода: {network_name}\nСтатус вывода: {withdraw}\nРазмер комиссии: {fee:.2f}

# binance


def send_profit53_messages(update, common_symbols53, ask_prices_gate1, bid_prices_binance):
    #withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits53 = []
    for symbol in common_symbols53:
        if ask_prices_gate1[symbol] == 0:
            profit53 = 0
        else:
            if ask_prices_gate1[symbol]:
                profit53 = (bid_prices_binance[symbol] - float(
                    ask_prices_gate1[symbol])) / float(ask_prices_gate1[symbol]) * 100
            else:
                # Обработка пустой строки
                continue
        profits53.append((symbol, profit53))

    # Сортировка списка по профиту в порядке убывания
    profits53.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit53 in profits53:
        if 0.5 <= profit53 <= 20:
            symbol1 = symbol.replace(
                "USDT", "_USDT")
            gate_url = f"https://www.gate.io/ru/trade/{symbol1}"
            binance_url = f"https://www.binance.com/ru/trade/{symbol}"
            symbol = symbol.split("_USDT")[0]
            #network_name, withdraw, fee = withdrawal_info[symbol]
            #fee = float(fee) * ask_prices_gate[symbol1]
            text = f"{symbol1}\n<a href='{gate_url}'>Покупка</a> на Gate = {ask_prices_gate1[symbol]}\n<a href='{binance_url}'>Продажа</a> на Binance = {bid_prices_binance[symbol]}\nСпред: {profit53:.2f}%"
            update.message.reply_html(text, disable_web_page_preview=True)

           # \nСеть вывода: {network_name}\nСтатус вывода: {withdraw}\nРазмер комиссии: {fee:.2f}

# bitget


def send_profit54_messages(update, common_symbols54, ask_prices_gate1, bid_prices_bitget):
    #withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits54 = []
    for symbol in common_symbols54:
        if ask_prices_gate1[symbol] == 0:
            profit54 = 0
        else:
            if ask_prices_gate1[symbol]:
                profit54 = (bid_prices_bitget[symbol] - float(
                    ask_prices_gate1[symbol])) / float(ask_prices_gate1[symbol]) * 100
            else:
                # Обработка пустой строки
                continue
        profits54.append((symbol, profit54))

    # Сортировка списка по профиту в порядке убывания
    profits54.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit54 in profits54:
        if 0.5 <= profit54 <= 20:
            symbol1 = symbol.replace(
                "USDT", "_USDT")
            gate_url = f"https://www.gate.io/ru/trade/{symbol1}"
            bitget_url = f"https://www.bitget.com/ru/spot/{symbol}_SPBL?type=spot"
            symbol = symbol.split("_USDT")[0]
            #network_name, withdraw, fee = withdrawal_info[symbol]
            #fee = float(fee) * ask_prices_gate[symbol1]
            text = f"{symbol1}\n<a href='{gate_url}'>Покупка</a> на Gate = {ask_prices_gate1[symbol]}\n<a href='{bitget_url}'>Продажа</a> на Bitget = {bid_prices_bitget[symbol]}\nСпред: {profit54:.2f}%"
            update.message.reply_html(text, disable_web_page_preview=True)

           # \nСеть вывода: {network_name}\nСтатус вывода: {withdraw}\nРазмер комиссии: {fee:.2f}

# Huobi


def send_profit56_messages(update, common_symbols65, ask_prices_gate1, bid_prices_huobi):
    #withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits53 = []
    for symbol in common_symbols65:
        if ask_prices_gate1[symbol] == 0:
            profit53 = 0
        else:
            if ask_prices_gate1[symbol]:
                profit53 = (bid_prices_huobi[symbol] - float(
                    ask_prices_gate1[symbol])) / float(ask_prices_gate1[symbol]) * 100
            else:
                # Обработка пустой строки
                continue
        profits53.append((symbol, profit53))

    # Сортировка списка по профиту в порядке убывания
    profits53.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit53 in profits53:
        if 0.5 <= profit53 <= 20:
            symbol1 = symbol.replace(
                "USDT", "_USDT")
            gate_url = f"https://www.gate.io/ru/trade/{symbol1}"
            hyuobi_url = f"https://www.huobi.com/ru-ru/trade/{symbol1}?type=spot"
            symbol = symbol.split("_USDT")[0]
            #network_name, withdraw, fee = withdrawal_info[symbol]
            #fee = float(fee) * ask_prices_gate[symbol1]
            text = f"{symbol1}\n<a href='{gate_url}'>Покупка</a> на Gate = {ask_prices_gate1[symbol]}\n<a href='{hyuobi_url}'>Продажа</a> на Huobi = {bid_prices_huobi[symbol]}\nСпред: {profit53:.2f}%"
            update.message.reply_html(text, disable_web_page_preview=True)

           # \nСеть вывода: {network_name}\nСтатус вывода: {withdraw}\nРазмер комиссии: {fee:.2f}
# Kucoin


def send_profit57_messages(update, common_symbols75, ask_prices_gate1, bid_prices_kucoin1):
    #withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits53 = []
    for symbol in common_symbols75:
        if ask_prices_gate1[symbol] == 0:
            profit53 = 0
        else:
            if ask_prices_gate1[symbol]:
                profit53 = (bid_prices_kucoin1[symbol] - float(
                    ask_prices_gate1[symbol])) / float(ask_prices_gate1[symbol]) * 100
            else:
                # Обработка пустой строки
                continue
        profits53.append((symbol, profit53))

    # Сортировка списка по профиту в порядке убывания
    profits53.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit53 in profits53:
        if 0.5 <= profit53 <= 20:
            symbol1 = symbol.replace(
                "USDT", "_USDT")
            symbol2 = symbol.replace(
                "USDT", "-USDT")
            gate_url = f"https://www.gate.io/ru/trade/{symbol1}"
            kucoin_url = f"https://www.kucoin.com/ru/trade/{symbol2}"
            symbol = symbol.split("_USDT")[0]
            #network_name, withdraw, fee = withdrawal_info[symbol]
            #fee = float(fee) * ask_prices_gate[symbol1]
            text = f"{symbol1}\n<a href='{gate_url}'>Покупка</a> на Gate = {ask_prices_gate1[symbol]}\n<a href='{kucoin_url}'>Продажа</a> на Kucoin = {bid_prices_kucoin1[symbol]}\nСпред: {profit53:.2f}%"
            update.message.reply_html(text, disable_web_page_preview=True)
