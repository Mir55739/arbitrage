import re
import requests
from MexcSDK.WitgdrowMexc import get_withdrawal_info
from Orderbook.Mexcy import calculate_average_price21
mexc_buy_enabled = True
mexc_sell_enabled = True
const = 5000


def get_ticker_data2():
    mexc = requests.get('https://www.mexc.com/open/api/v2/market/ticker')
    ticker_data2 = mexc.json()
    return ticker_data2


def get_prices_mexc(ticker_data2):
    ticker_all2 = ticker_data2['data']
    ask_prices_mexc = {ticker['symbol']: float(
        ticker['ask']) for ticker in ticker_all2}
    bid_prices_mexc = {ticker['symbol']: float(
        ticker['bid']) for ticker in ticker_all2}
    ask_prices_mexc1 = {symbol.replace(
        "_", ""): price for symbol, price in ask_prices_mexc.items()}
    bid_prices_mexc1 = {symbol.replace(
        "_", ""): price for symbol, price in bid_prices_mexc.items()}
    return ask_prices_mexc, bid_prices_mexc, ask_prices_mexc1, bid_prices_mexc1


# ////////////////////////////////////////////////////////////////////////
# Bitmart
def send_profit21_messages(update, common_symbols, ask_prices_mexc, bid_prices_bitmart):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits2 = []
    for symbol in common_symbols:
        if ask_prices_mexc[symbol] == 0:
            profit2 = 0
        else:
            profit2 = (
                bid_prices_bitmart[symbol] - ask_prices_mexc[symbol]) / ask_prices_mexc[symbol] * 100
        profits2.append((symbol, profit2))

    # Сортировка списка по профиту в порядке убывания
    profits2.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit2 in profits2:
        if 0.5 <= profit2 <= 20:
            mexc_url = f"https://www.mexc.com/ru-RU/exchange/{symbol}"
            bitmart_url = f"https://www.bitmart.com/trade/ru-RU?layout=basic&theme=dark&symbol={symbol}"
            symbol1 = symbol
            symbol = symbol.split("_USDT")[0]
            volume_in_coins = const/float(ask_prices_mexc[symbol1])
            step_usdt = const/(const*10)
            network_name, withdraw, fee = withdrawal_info[symbol]
            fee = float(fee) * ask_prices_mexc[symbol1]
            text = f"{symbol1}\n<a href='{mexc_url}'>Покупка</a> на MEXC = {ask_prices_mexc[symbol1]}\n<a href='{bitmart_url}'>Продажа</a> на Bitmart = {bid_prices_bitmart[symbol1]}\nСпред: {profit2:.2f}%\nСеть вывода: {network_name}\nСтатус вывода: {withdraw}\nРазмер комиссии: {fee:.2f}"
            best_ask_volume, best_ask_price, best_ask_orders, best_bid_volume, best_bid_price, best_bid_orders, best_profit = calculate_average_price21(
                symbol, volume_in_coins, step_usdt)
            best_profit = best_profit-fee
            if best_profit > 0:
                text += f"\nЛучший вариант: покупка {best_ask_volume:.2f} USDT по средней цене {best_ask_price:.8f} ({best_ask_orders} ордеров) и продажа {best_bid_volume:.2f} USDT по средней цене {best_bid_price:.8f} ({best_bid_orders} ордеров). Прибыль: {best_profit:.2f} USDT"
            else:
                text += f"\nЛимитная покупка и продажа"
            update.message.reply_html(text, disable_web_page_preview=True)
            calculate_profit(symbol, fee)


def calculate_profit(symbol, fee):
    # Получаем стаканы котировок с двух бирж (Bitmart и Mexc)
    URL1 = f"https://api-cloud.bitmart.com/spot/v1/symbols/book?symbol={symbol}_USDT&depth=10"
    URL2 = f"https://api.mexc.com/api/v3/depth?symbol={symbol}USDT&limit=10"
    response1 = requests.get(URL1).json()
    response2 = requests.get(URL2).json()
    # Получаем информацию о лучшем спросе на Mex
    ask_mexc = response2['asks']
    total_ask_mexc_volume = sum(float(x[1]) for x in ask_mexc)

    # Получаем информацию о лучшем предложении на Bitmart
    bid_bitmart = response1['data']['buys']
    total_bid_bitmart_volume = sum(float(x['amount']) for x in bid_bitmart)

    # Считаем прибыль для каждой комбинации ордеров
    max_profit = 0
    buy_amounts = []
    sell_amounts = []
    best_buy_order = 0
    best_sell_order = 0
    buy_volume_usdt = 0
    sell_volume_usdt = 0
    mean_sell_price = 0
    mean_buy_price = 0
    for i in range(1, 11):  # Bitmart buy
        bitmart_price = float(bid_bitmart[i-1]['price'])
        bitmart_volume = float(bid_bitmart[i-1]['amount'])

        for j in range(1, 11):  # Mexc sell
            mexc_price = float(ask_mexc[j-1][0])
            mexc_volume = float(ask_mexc[j-1][1])

            # Вычисляем объем продажи
            sell_volume = min(bitmart_volume, mexc_volume,
                              total_ask_mexc_volume)

            # Рассчитываем стоимость покупки на Bitmart и продажи на Mexc
            bitmart_cost = sell_volume * bitmart_price
            mexc_revenue = sell_volume * mexc_price

            # Рассчитываем прибыль
            profit = bitmart_cost - mexc_revenue - float(fee)

            # Обновляем максимальную прибыль
            if profit > max_profit:

                max_profit = profit

                # Сохраняем информацию о лучшей комбинации ордеров
                best_buy_order = i
                best_sell_order = j

                # Сохраняем информацию о средней цене покупки, объеме продажи и средней цене продажи
                mean_buy_price = sum([float(x['price'])
                                      for x in bid_bitmart[:i]]) / i
                mean_sell_price = sum([float(x[0]) for x in ask_mexc[:j]]) / j
                buy_volume_usdt = sell_volume*mean_sell_price
                sell_volume_usdt = sell_volume*mean_buy_price

    return max_profit, best_buy_order, best_sell_order, buy_volume_usdt, sell_volume_usdt, mean_sell_price, mean_buy_price
# Binance


def send_profit23_messages(update, common_symbols2, ask_prices_mexc1, bid_prices_binance):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits23 = []
    for symbol in common_symbols2:
        if ask_prices_mexc1[symbol] == 0:
            profit23 = 0
        else:
            profit23 = (
                bid_prices_binance[symbol] - ask_prices_mexc1[symbol]) / ask_prices_mexc1[symbol] * 100
        profits23.append((symbol, profit23))

    # Сортировка списка по профиту в порядке убывания
    profits23.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit23 in profits23:
        if 0.5 <= profit23 <= 20:
            mexc_url = f"https://www.mexc.com/ru-RU/exchange/{symbol}"
            binance_url = f"https://www.binance.com/ru/trade/{symbol}"
            symbol1 = symbol
            symbol = re.split('USDT|USDC|BTC|ETH', symbol)[0]
            network_name, withdraw, fee = withdrawal_info[symbol]
            fee = float(fee) * ask_prices_mexc1[symbol1]
            text = f"{symbol1}\n<a href='{mexc_url}'>Покупка</a> на MEXC = {ask_prices_mexc1[symbol1]}\n<a href='{binance_url}'>Продажа</a> на Binance = {bid_prices_binance[symbol1]}\nСпред: {profit23:.2f}%\nСеть вывода: {network_name}\nСтатус вывода: {withdraw}\nРазмер комиссии: {fee:.2f}"
            update.message.reply_html(text, disable_web_page_preview=True)

# Bitget


def send_profit24_messages(update, common_symbols24, ask_prices_mexc1, bid_prices_bitget):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits24 = []
    for symbol in common_symbols24:
        if ask_prices_mexc1[symbol] == 0:
            profit24 = 0
        else:
            profit24 = (
                bid_prices_bitget[symbol] - ask_prices_mexc1[symbol]) / ask_prices_mexc1[symbol] * 100
        profits24.append((symbol, profit24))

    # Сортировка списка по профиту в порядке убывания
    profits24.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit24 in profits24:
        if 0.5 <= profit24 <= 20:
            mexc_url = f"https://www.mexc.com/ru-RU/exchange/{symbol}"
            bitget_url = f"https://www.bitget.com/ru/spot/{symbol}_SPBL?type=spot"
            symbol1 = symbol
            symbol = re.split('USDT|USDC|BTC|ETH', symbol)[0]
            network_name, withdraw, fee = withdrawal_info[symbol]
            fee = float(fee) * ask_prices_mexc1[symbol1]
            text = f"{symbol1}\n<a href='{mexc_url}'>Покупка</a> на MEXC = {ask_prices_mexc1[symbol1]}\n<a href='{bitget_url}'>Продажа</a> на Bitget = {bid_prices_bitget[symbol1]}\nСпред: {profit24:.2f}%\nСеть вывода: {network_name}\nСтатус вывода: {withdraw}\nРазмер комиссии: {fee:.2f}"
            update.message.reply_html(text, disable_web_page_preview=True)

# Gate


def send_profit25_messages(update, common_symbols52, ask_prices_mexc, bid_prices_gate):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits23 = []
    for symbol in common_symbols52:
        if ask_prices_mexc[symbol] == 0 or not ask_prices_mexc[symbol] or not bid_prices_gate[symbol]:
            profit23 = 0
        else:
            profit23 = (float(bid_prices_gate[symbol]) - float(
                ask_prices_mexc[symbol])) / float(ask_prices_mexc[symbol]) * 100
        profits23.append((symbol, profit23))

    # Сортировка списка по профиту в порядке убывания
    profits23.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit23 in profits23:
        if 0.5 <= profit23 <= 20:
            mexc_url = f"https://www.mexc.com/ru-RU/exchange/{symbol}"
            gate_url = f"https://www.gate.io/ru/trade/{symbol}"
            symbol1 = symbol
            symbol = symbol.split("_USDT")[0]
            if symbol in withdrawal_info:
                network_name, withdraw, fee = withdrawal_info[symbol]
                fee = float(fee) * ask_prices_mexc[symbol1]
            else:
                # Обработка случая, когда ключа нет в словаре
                network_name = "Неизвестно"
                withdraw = "Неизвестно"
                fee = 0
            text = f"{symbol1}\n<a href='{mexc_url}'>Покупка</a> на MEXC = {ask_prices_mexc[symbol1]}\n<a href='{gate_url}'>Продажа</a> на Gate = {bid_prices_gate[symbol1]}\nСпред: {profit23:.2f}%\nСеть вывода: {network_name}\nСтатус вывода: {withdraw}\nРазмер комиссии: {fee:.2f}"
            update.message.reply_html(text, disable_web_page_preview=True)

# Huobi


def send_profit26_messages(update, common_symbols62, ask_prices_mexc1, bid_prices_huobi):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits23 = []
    for symbol in common_symbols62:
        if ask_prices_mexc1[symbol] == 0:
            profit23 = 0
        else:
            profit23 = (
                bid_prices_huobi[symbol] - ask_prices_mexc1[symbol]) / ask_prices_mexc1[symbol] * 100
        profits23.append((symbol, profit23))

    # Сортировка списка по профиту в порядке убывания
    profits23.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit23 in profits23:
        if 0.5 <= profit23 <= 20:
            symbol2 = symbol.replace('USDT', '_USDT').lower()
            mexc_url = f"https://www.mexc.com/ru-RU/exchange/{symbol2}"
            hyuobi_url = f"https://www.huobi.com/ru-ru/trade/{symbol2}?type=spot"
            symbol1 = symbol
            symbol = re.split('USDT|USDC|BTC|ETH', symbol)[0]
            network_name, withdraw, fee = withdrawal_info[symbol]
            fee = float(fee) * ask_prices_mexc1[symbol1]
            text = f"{symbol1}\n<a href='{mexc_url}'>Покупка</a> на MEXC = {ask_prices_mexc1[symbol1]}\n<a href='{hyuobi_url}'>Продажа</a> на Huobi = {bid_prices_huobi[symbol1]}\nСпред: {profit23:.2f}%\nСеть вывода: {network_name}\nСтатус вывода: {withdraw}\nРазмер комиссии: {fee:.2f}"
            update.message.reply_html(text, disable_web_page_preview=True)

# Kucoin


def send_profit27_messages(update, common_symbols72, ask_prices_mexc1, bid_prices_kucoin1):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits23 = []
    for symbol in common_symbols72:
        if ask_prices_mexc1[symbol] == 0:
            profit23 = 0
        else:
            profit23 = (
                bid_prices_kucoin1[symbol] - ask_prices_mexc1[symbol]) / ask_prices_mexc1[symbol] * 100
        profits23.append((symbol, profit23))

    # Сортировка списка по профиту в порядке убывания
    profits23.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit23 in profits23:
        if 0.5 <= profit23 <= 20:
            symbol2 = symbol.replace(
                "USDT", "_USDT")
            mexc_url = f"https://www.mexc.com/ru-RU/exchange/{symbol2}"
            symbol1 = symbol.replace(
                "USDT", "-USDT")
            kucoin_url = f"https://www.kucoin.com/ru/trade/{symbol1}"
            symbol1 = symbol
            symbol = re.split('USDT|USDC|BTC|ETH', symbol)[0]
            try:
                network_name, withdraw, fee = withdrawal_info[symbol]
            except KeyError:
                network_name = "Неизвестно"
                withdraw = "Неизвестно"
                fee = 0
            fee = float(fee) * ask_prices_mexc1[symbol1]
            text = f"{symbol1}\n<a href='{mexc_url}'>Покупка</a> на MEXC = {ask_prices_mexc1[symbol1]}\n<a href='{kucoin_url}'>Продажа</a> на Kucoin = {bid_prices_kucoin1[symbol1]}\nСпред: {profit23:.2f}%\nСеть вывода: {network_name}\nСтатус вывода: {withdraw}\nРазмер комиссии: {fee:.2f}"
            update.message.reply_html(text, disable_web_page_preview=True)
