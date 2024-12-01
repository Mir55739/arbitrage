from Orderbook.Bitmarty import calculate_average_price12, calculate_average_price14,calculate_average_price13
from common import const
import requests
import re
from Mexc import get_prices_mexc, get_ticker_data2
import time
from BitmartSDK.bitmart.cloud_log import CloudLog
from BitmartSDK.bitmart.api_account import APIAccount
CloudLog.set_logger_level('info')
api_key = "e2ce0607ec00afed2176c7e8e9eb6b25d4fd921b"
secret_key = "a8ba97b8fd1cb5393a25812fefa82c0171871474d9dbdae5e6e5bc573421e5b2"
memo = "Your Memo"
bitmart_buy_enabled = True
bitmart_sell_enabled = True


def get_ticker_data():
    bitmart = requests.get('https://api-cloud.bitmart.com/spot/v2/ticker')
    ticker_data = bitmart.json()
    return ticker_data


def get_prices_bitmart(ticker_data):
    ticker_all = ticker_data['data']['tickers']
    ask_prices_bitmart = {ticker['symbol']: float(
        ticker['best_ask']) for ticker in ticker_all}
    bid_prices_bitmart = {ticker['symbol']: float(
        ticker['best_bid']) for ticker in ticker_all}
# Без "_"
    ask_prices_bitmart1 = {symbol.replace(
        "_", ""): price for symbol, price in ask_prices_bitmart.items()}
    bid_prices_bitmart1 = {symbol.replace(
        "_", ""): price for symbol, price in bid_prices_bitmart.items()}
    return ask_prices_bitmart, bid_prices_bitmart, ask_prices_bitmart1, bid_prices_bitmart1


# ///////////////////////////////////////////////////////////////////


def send_profit12_messages(update, common_symbols, ask_prices_bitmart, bid_prices_mexc, api_key, secret_key, memo):
    # Создание списка кортежей (символ, профит1)
    profits1 = []
    for symbol in common_symbols:
        if ask_prices_bitmart[symbol] == 0:
            profit1 = 0
        else:
            profit1 = (
                bid_prices_mexc[symbol] - ask_prices_bitmart[symbol]) / ask_prices_bitmart[symbol] * 100
        profits1.append((symbol, profit1))

    # Сортировка списка по профиту в порядке убывания
    profits1.sort(key=lambda x: x[1], reverse=True)

    # Отправка сообщений для первого условия в отсортированном порядке
    for symbol, profit1 in profits1:
        if 0.5 <= profit1 <= 20:
            bitmart_url = f"https://www.bitmart.com/trade/ru-RU?layout=basic&theme=dark&symbol={symbol}"
            mexc_url = f"https://www.mexc.com/ru-RU/exchange/{symbol}"
            symbol1 = symbol.split("_")[0]
            volume_in_coins = const/float(ask_prices_bitmart[symbol])
            step_usdt = const/(const*10)
            # Получение комиссии за вывод для символа
            try:
                contracAPI = APIAccount(
                    api_key, secret_key, memo, timeout=(3, 10))
                r = contracAPI.get_withdraw_charge(symbol1)
                body = r[0]
                withdraw_fee = body['data']['withdraw_fee']
                fee_dol = f"Комиссия за вывод для {symbol1}: {round(float(withdraw_fee)*float(ask_prices_bitmart[symbol]), 2)}"

            except Exception as e:
                fee_dol = f"Вывод токена {symbol1} закрыт"

            text = f"{symbol}\n<a href='{bitmart_url}'>Покупка</a> на Bitmart = {ask_prices_bitmart[symbol]} \n<a href='{mexc_url}'>Продажа</a> на Mexc = {bid_prices_mexc[symbol]}\nСпред: {profit1:.2f}%\n{fee_dol}\n"
            best_ask_volume, best_ask_price, best_ask_orders, best_bid_volume, best_bid_price, best_bid_orders, best_profit = calculate_average_price12(
                symbol1, volume_in_coins, step_usdt)
            coms = float(best_profit)-(float(withdraw_fee)
                                       * float(ask_prices_bitmart[symbol]))
            if coms > 0:
                text += f"\nЛучший вариант: покупка {best_ask_volume:.2f} USDT по средней цене {best_ask_price:.2e} ({best_ask_orders} ордеров) и продажа {best_bid_volume:.2f} USDT по средней цене {best_bid_price:.2e} ({best_bid_orders} ордеров). Прибыль: {coms:.2f} USDT  "
            else:
                text += f"\n Лимитная покупка и продажа"
            update.message.reply_html(text, disable_web_page_preview=True)
            # Добавляем задержку между запросами
            time.sleep(0.5)

# Binance


def send_profit13_messages(update, common_symbols1, ask_prices_bitmart1, bid_prices_binance, api_key, secret_key, memo):
    # Создание списка кортежей (символ, профит1)
    profits13 = []
    for symbol in common_symbols1:
        if ask_prices_bitmart1.get(symbol, 0) == 0:
            profit13 = 0
        else:
            profit13 = (
                bid_prices_binance[symbol] - ask_prices_bitmart1[symbol]) / ask_prices_bitmart1[symbol] * 100
        profits13.append((symbol, profit13))

    # Сортировка списка по профиту в порядке убывания
    profits13.sort(key=lambda x: x[1], reverse=True)

    # Отправка сообщений для первого условия в отсортированном порядке
    for symbol, profit13 in profits13:
        if 0.5 <= profit13 <= 20:
            bitmart_url = f"https://www.bitmart.com/trade/ru-RU?layout=basic&theme=dark&symbol={symbol}"
            binance_url = f"https://www.binance.com/ru/trade/{symbol}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            volume_in_coins = const/float(ask_prices_bitmart1[symbol])
            step_usdt = const/(const*10)
            # Получение комиссии за вывод для символа
            try:
                contracAPI = APIAccount(
                    api_key, secret_key, memo, timeout=(3, 10))
                r = contracAPI.get_withdraw_charge(base_symbol)
                body = r[0]
                withdraw_fee = body['data']['withdraw_fee']
                fee_dol = f"Комиссия за вывод для {base_symbol}: {round(float(withdraw_fee)*float(ask_prices_bitmart1[symbol]), 2)}"
                # print(
                # f"Комиссия за вывод для {symbol1}: {float(withdraw_fee)*float(ask_prices_bitmart[symbol])}")
            except Exception as e:
                fee_dol = f"Вывод токена {base_symbol} закрыт"
                # print(
                # f"Вывод токена {symbol1} закрыт")
            text = f"{symbol}\n<a href='{bitmart_url}'>Покупка</a> на Bitmart = {ask_prices_bitmart1[symbol]} \n<a href='{binance_url}'>Продажа</a> на Binance = {bid_prices_binance[symbol]}\nСпред: {profit13:.2f}%\n{fee_dol}\n"
            best_ask_volume, best_ask_price, best_ask_orders, best_bid_volume, best_bid_price, best_bid_orders, best_profit = calculate_average_price13(base_symbol, volume_in_coins, step_usdt)
            coms = float(best_profit)-(float(withdraw_fee)
                                       * float(ask_prices_bitmart1[symbol]))
            if coms > 0:
                text += f"\nЛучший вариант: покупка {best_ask_volume:.2f} USDT по средней цене {best_ask_price:.2e} ({best_ask_orders} ордеров) и продажа {best_bid_volume:.2f} USDT по средней цене {best_bid_price:.2e} ({best_bid_orders} ордеров). Прибыль: {coms:.2f} USDT  "
            else:
                text += f"\n Лимитная покупка и продажа"
            update.message.reply_html(text, disable_web_page_preview=True)
            # Добавляем задержку между запросами
            time.sleep(0.5)

# Bitget


def send_profit14_messages(update, common_symbols41, ask_prices_bitmart1, bid_prices_bitget, api_key, secret_key, memo):
    # Создание списка кортежей (символ, профит1)
    profits14 = []
    for symbol in common_symbols41:
        if ask_prices_bitmart1.get(symbol, 0) == 0:
            profit14 = 0
        else:
            profit14 = (
                bid_prices_bitget[symbol] - ask_prices_bitmart1[symbol]) / ask_prices_bitmart1[symbol] * 100
        profits14.append((symbol, profit14))

    # Сортировка списка по профиту в порядке убывания
    profits14.sort(key=lambda x: x[1], reverse=True)

    # Отправка сообщений для первого условия в отсортированном порядке
    for symbol, profit14 in profits14:
        if 0.5 <= profit14 <= 20:
            bitmart_url = f"https://www.bitmart.com/trade/ru-RU?layout=basic&theme=dark&symbol={symbol}"
            bitget_url = f"https://www.bitget.com/ru/mix/usdt/{symbol}_UMCBL"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            symbol1 = symbol.split("_")[0]
            volume_in_coins = const/float(ask_prices_bitmart1[symbol])
            step_usdt = const/(const*10)
            # Получение комиссии за вывод для символа
            try:
                contracAPI = APIAccount(
                    api_key, secret_key, memo, timeout=(3, 10))
                r = contracAPI.get_withdraw_charge(base_symbol)
                body = r[0]
                withdraw_fee = body['data']['withdraw_fee']
                fee_dol = f"Комиссия за вывод для {base_symbol}: {round(float(withdraw_fee)*float(ask_prices_bitmart1[symbol]), 2)}"
            except Exception as e:
                fee_dol = f"Вывод токена {base_symbol} закрыт"
            text = f"{symbol}\n<a href='{bitmart_url}'>Покупка</a> на Bitmart = {ask_prices_bitmart1[symbol]} \n<a href='{bitget_url}'>Продажа</a> на Bitget = {bid_prices_bitget[symbol]}\nСпред: {profit14:.2f}%\n{fee_dol}\n"
            best_ask_volume, best_ask_price, best_ask_orders, best_bid_volume, best_bid_price, best_bid_orders, best_profit = calculate_average_price14(base_symbol, volume_in_coins, step_usdt)
            coms = float(best_profit)-(float(withdraw_fee)
                                       * float(ask_prices_bitmart1[symbol]))
            if coms > 0:
                text += f"\nЛучший вариант: покупка {best_ask_volume:.2f} USDT по средней цене {best_ask_price:.2e} ({best_ask_orders} ордеров) и продажа {best_bid_volume:.2f} USDT по средней цене {best_bid_price:.2e} ({best_bid_orders} ордеров). Прибыль: {coms:.2f} USDT  "
            else:
                text += f"\n Лимитная покупка и продажа"
            update.message.reply_html(text, disable_web_page_preview=True)
            # Добавляем задержку между запросами
            time.sleep(0.5)

# Gate


def send_profit15_messages(update, common_symbols51, ask_prices_bitmart, bid_prices_gate, api_key, secret_key, memo):
    # Создание списка кортежей (символ, профит1)
    profits1 = []
    for symbol in common_symbols51:
        if ask_prices_bitmart[symbol] == 0 or not ask_prices_bitmart[symbol] or not bid_prices_gate[symbol]:
            profit1 = 0
        else:
            profit1 = (float(bid_prices_gate[symbol]) - float(
                ask_prices_bitmart[symbol])) / float(ask_prices_bitmart[symbol]) * 100
        profits1.append((symbol, profit1))

    # Сортировка списка по профиту в порядке убывания
    profits1.sort(key=lambda x: x[1], reverse=True)

    # Отправка сообщений для первого условия в отсортированном порядке
    for symbol, profit1 in profits1:
        if 0.5 <= profit1 <= 20:
            bitmart_url = f"https://www.bitmart.com/trade/ru-RU?layout=basic&theme=dark&symbol={symbol}"
            gate_url = f"https://www.gate.io/ru/trade/{symbol}"
            symbol1 = symbol.split("_")[0]
            # Получение комиссии за вывод для символа
            try:
                contracAPI = APIAccount(
                    api_key, secret_key, memo, timeout=(3, 10))
                r = contracAPI.get_withdraw_charge(symbol1)
                body = r[0]
                withdraw_fee = body['data']['withdraw_fee']
                fee_dol = f"Комиссия за вывод для {symbol1}: {round(float(withdraw_fee)*float(ask_prices_bitmart[symbol]), 2)}"
                # print(
                # f"Комиссия за вывод для {symbol1}: {float(withdraw_fee)*float(ask_prices_bitmart[symbol])}")
            except Exception as e:
                fee_dol = f"Вывод токена {symbol1} закрыт"
                # print(
                # f"Вывод токена {symbol1} закрыт")
            text = f"{symbol}\n<a href='{bitmart_url}'>Покупка</a> на Bitmart = {ask_prices_bitmart[symbol]} \n<a href='{gate_url}'>Продажа</a> на Gate = {bid_prices_gate[symbol]}\nСпред: {profit1:.2f}%\n{fee_dol}\n"
            update.message.reply_html(text, disable_web_page_preview=True)
            # Добавляем задержку между запросами
            time.sleep(0.5)

# Huobi


def send_profit16_messages(update, common_symbols61, ask_prices_bitmart1, bid_prices_huobi, api_key, secret_key, memo):
    # Создание списка кортежей (символ, профит1)
    profits13 = []
    for symbol in common_symbols61:
        if ask_prices_bitmart1.get(symbol, 0) == 0:
            profit13 = 0
        else:
            profit13 = (
                bid_prices_huobi[symbol] - ask_prices_bitmart1[symbol]) / ask_prices_bitmart1[symbol] * 100
        profits13.append((symbol, profit13))

    # Сортировка списка по профиту в порядке убывания
    profits13.sort(key=lambda x: x[1], reverse=True)

    # Отправка сообщений для первого условия в отсортированном порядке
    for symbol, profit13 in profits13:
        if 0.5 <= profit13 <= 20:
            symbol1 = symbol.replace('USDT', '_USDT').lower()
            symbol2 = symbol.replace('USDT', '_USDT')
            bitmart_url = f"https://www.bitmart.com/trade/ru-RU?layout=basic&theme=dark&symbol={symbol2}"
            hyuobi_url = f"https://www.huobi.com/ru-ru/trade/{symbol1}?type=spot"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            # Получение комиссии за вывод для символа
            try:
                contracAPI = APIAccount(
                    api_key, secret_key, memo, timeout=(3, 10))
                r = contracAPI.get_withdraw_charge(base_symbol)
                body = r[0]
                withdraw_fee = body['data']['withdraw_fee']
                fee_dol = f"Комиссия за вывод для {base_symbol}: {round(float(withdraw_fee)*float(ask_prices_bitmart1[symbol]), 2)}"
                # print(
                # f"Комиссия за вывод для {symbol1}: {float(withdraw_fee)*float(ask_prices_bitmart[symbol])}")
            except Exception as e:
                fee_dol = f"Вывод токена {base_symbol} закрыт"
                # print(
                # f"Вывод токена {symbol1} закрыт")
            text = f"{symbol}\n<a href='{bitmart_url}'>Покупка</a> на Bitmart = {ask_prices_bitmart1[symbol]} \n<a href='{hyuobi_url}'>Продажа</a> на Huobi = {bid_prices_huobi[symbol]}\nСпред: {profit13:.2f}%\n{fee_dol}\n"
            update.message.reply_html(text, disable_web_page_preview=True)
            # Добавляем задержку между запросами
            time.sleep(0.5)

# Kucoin


def send_profit17_messages(update, common_symbols71, ask_prices_bitmart1, bid_prices_kucoin, api_key, secret_key, memo):
    # Создание списка кортежей (символ, профит1)
    profits13 = []
    for symbol in common_symbols71:
        if ask_prices_bitmart1.get(symbol, 0) == 0:
            profit13 = 0
        else:
            bid_prices_kucoin1 = {symbol.replace(
                "-", ""): price for symbol, price in bid_prices_kucoin.items()}
            profit13 = (
                bid_prices_kucoin1[symbol] - ask_prices_bitmart1[symbol]) / ask_prices_bitmart1[symbol] * 100
        profits13.append((symbol, profit13))

    # Сортировка списка по профиту в порядке убывания
    profits13.sort(key=lambda x: x[1], reverse=True)

    # Отправка сообщений для первого условия в отсортированном порядке
    for symbol, profit13 in profits13:
        if 0.5 <= profit13 <= 20:
            symbol1 = symbol.replace(
                "USDT", "-USDT")
            symbol2 = symbol.replace(
                "USDT", "_USDT")
            bitmart_url = f"https://www.bitmart.com/trade/ru-RU?layout=basic&theme=dark&symbol={symbol2}"
            kucoin_url = f"https://www.kucoin.com/ru/trade/{symbol1}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            volume_in_coins = const/float(ask_prices_bitmart1[symbol])
            step_usdt = const/(const*10)
            # Получение комиссии за вывод для символа
            try:
                contracAPI = APIAccount(
                    api_key, secret_key, memo, timeout=(3, 10))
                r = contracAPI.get_withdraw_charge(base_symbol)
                body = r[0]
                withdraw_fee = body['data']['withdraw_fee']
                fee_dol = f"Комиссия за вывод для {base_symbol}: {round(float(withdraw_fee)*float(ask_prices_bitmart1[symbol]), 2)}"
            except Exception as e:
                fee_dol = f"Вывод токена {base_symbol} закрыт"
            text = f"{symbol}\n<a href='{bitmart_url}'>Покупка</a> на Bitmart = {ask_prices_bitmart1[symbol]} \n<a href='{kucoin_url}'>Продажа</a> на Kucoin = {bid_prices_kucoin1[symbol]}\nСпред: {profit13:.2f}%\n{fee_dol}\n"

            # best_ask_volume, best_ask_price, best_ask_orders, best_bid_volume, best_bid_price, best_bid_orders, best_profit = calculate_average_price17(
            #   base_symbol, volume_in_coins, step_usdt)
           # text += f"\n{base_symbol} \nЛучший вариант: покупка {best_ask_volume:.2f} USDT по средней цене {best_ask_price:.6f} ({best_ask_orders} ордеров) и продажа {best_bid_volume:.2f} USDT по средней цене {best_bid_price:.6f} ({best_bid_orders} ордеров). Прибыль: {best_profit:.2f} USDT"

            update.message.reply_html(text, disable_web_page_preview=True)
            # Добавляем задержку между запросами
            time.sleep(0.5)
