import re
from binance.client import Client
from WithdrawBinance import get_withdrawal_info
api_key = 'OT4G3dLSVNEa5vXN3RL6BVlMzhDncWvzvFZu5hOF2oGY2qsoWqqz5u2BHIbGapAH'
api_secret = '32bTDTmCq9S03jM1eYwAlkHmY31UUyeUGWB8CIOfgJ8EgNvgAnTLXCGHSrpkdCr2'
binance_buy_enabled = True
binance_sell_enabled = True


def get_ticker_data3():
    client = Client(api_key, api_secret)
    ticker_all3 = client.get_orderbook_tickers()
    return ticker_all3


def get_prices_binance(ticker_all3):
    ask_prices_binance = {ticker['symbol']: float(
        ticker['askPrice']) for ticker in ticker_all3}
    bid_prices_binance = {ticker['symbol']: float(
        ticker['bidPrice']) for ticker in ticker_all3}
   # print(bid_prices_binance)
    return ask_prices_binance, bid_prices_binance

# //////////////////////////////////////////////////////////////////
# Bitmart


def send_profit31_messages(update, common_symbols1, ask_prices_binance, bid_prices_bitmart1):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits3 = []
    for symbol in common_symbols1:
        if symbol in ask_prices_binance:
            if ask_prices_binance[symbol] == 0:
                profit3 = 0
            else:
                profit3 = (
                    bid_prices_bitmart1[symbol] - ask_prices_binance[symbol]) / ask_prices_binance[symbol] * 100
        else:
            profit3 = 0
        profits3.append((symbol, profit3))
        # Сортировка списка по профиту в порядке убывания
    profits3.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit3 in profits3:
        if 0.5 <= profit3 <= 20:
            binance_url = f"https://www.binance.com/ru/trade/{symbol}"
            bitmart_url = f"https://www.bitmart.com/trade/ru-RU?layout=basic&theme=dark&symbol={symbol}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            withdraw_fee = withdrawal_info[base_symbol]
            withdraw_fee = float(withdraw_fee) * \
                ask_prices_binance[symbol]
            text = f"{symbol}\n<a href='{binance_url}'>Покупка</a> на Binance = {ask_prices_binance[symbol]}\n<a href='{bitmart_url}'>Продажа</a> на Bitmart = {bid_prices_bitmart1[symbol]}\nСпред: {profit3:.2f}%\n\nРазмер комиссии: {withdraw_fee:.2f}"
            update.message.reply_html(
                text, disable_web_page_preview=True)

# Mexc


def send_profit32_messages(update, common_symbols2, ask_prices_binance, bid_prices_mexc1):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits32 = []
    for symbol in common_symbols2:
        if symbol in ask_prices_binance:
            if ask_prices_binance[symbol] == 0:
                profit32 = 0
            else:
                profit32 = (
                    bid_prices_mexc1[symbol] - ask_prices_binance[symbol]) / ask_prices_binance[symbol] * 100
        else:
            profit32 = 0
        profits32.append((symbol, profit32))
        # Сортировка списка по профиту в порядке убывания
    profits32.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit32 in profits32:
        if 0.5 <= profit32 <= 20:
            binance_url = f"https://www.binance.com/ru/trade/{symbol}"
            mexc_url = f"https://www.mexc.com/ru-RU/exchange/{symbol}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            withdraw_fee = withdrawal_info[base_symbol]
            withdraw_fee = float(withdraw_fee) * \
                ask_prices_binance[symbol]
            text = f"{symbol}\n<a href='{binance_url}'>Покупка</a> на Binance = {ask_prices_binance[symbol]}\n<a href='{mexc_url}'>Продажа</a> на Mexc = {bid_prices_mexc1[symbol]}\nСпред: {profit32:.2f}%\n\nРазмер комиссии: {withdraw_fee:.2f}"
            update.message.reply_html(
                text, disable_web_page_preview=True)

# Bitget


def send_profit34_messages(update, common_symbols34, ask_prices_binance, bid_prices_bitget):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits34 = []
    for symbol in common_symbols34:
        if symbol in ask_prices_binance:
            if ask_prices_binance[symbol] == 0:
                profit34 = 0
            else:
                profit34 = (
                    bid_prices_bitget[symbol] - ask_prices_binance[symbol]) / ask_prices_binance[symbol] * 100
        else:
            profit34 = 0
        profits34.append((symbol, profit34))
        # Сортировка списка по профиту в порядке убывания
    profits34.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit34 in profits34:
        if 0.5 <= profit34 <= 20:
            binance_url = f"https://www.binance.com/ru/trade/{symbol}"
            bitget_url = f"https://www.bitget.com/ru/spot/{symbol}_SPBL?type=spot"
            base_symbol = re.split('USDC|USDT|ETH|BTC|TRY', symbol)[0]
            withdraw_fee = withdrawal_info[base_symbol]
            withdraw_fee = float(withdraw_fee) * \
                ask_prices_binance[symbol]
            text = f"{symbol}\n<a href='{binance_url}'>Покупка</a> на Binance = {ask_prices_binance[symbol]}\n<a href='{bitget_url}'>Продажа</a> на Bitget = {bid_prices_bitget[symbol]}\nСпред: {profit34:.2f}%\n\nРазмер комиссии: {withdraw_fee:.2f}"
            update.message.reply_html(
                text, disable_web_page_preview=True)

# Gate


def send_profit35_messages(update, common_symbols53, ask_prices_binance, bid_prices_gate1):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits3 = []
    for symbol in common_symbols53:
        if symbol in ask_prices_binance:
            if ask_prices_binance[symbol] == 0 or not ask_prices_binance[symbol] or not bid_prices_gate1[symbol]:
                profit3 = 0
            else:
                profit3 = (float(
                    bid_prices_gate1[symbol]) - ask_prices_binance[symbol]) / ask_prices_binance[symbol] * 100
        else:
            profit3 = 0
        profits3.append((symbol, profit3))
    # Сортировка списка по профиту в порядке убывания
    profits3.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit3 in profits3:
        if 0.5 <= profit3 <= 20:
            binance_url = f"https://www.binance.com/ru/trade/{symbol}"
            gate_url = f"https://www.gate.io/ru/trade/{symbol}"
            base_symbol = re.split('USDC|USDT|ETH|BTC|TRY', symbol)[0]
            if base_symbol:
                withdraw_fee = withdrawal_info[base_symbol]
                withdraw_fee = float(withdraw_fee) * ask_prices_binance[symbol]
            else:
                # Обработка случая, когда base_symbol является пустой строкой
                withdraw_fee = 0
            text = f"{symbol}\n<a href='{binance_url}'>Покупка</a> на Binance = {ask_prices_binance[symbol]}\n<a href='{gate_url}'>Продажа</a> на Gate = {bid_prices_gate1[symbol]}\nСпред: {profit3:.2f}%\n\nРазмер комиссии: {withdraw_fee:.2f}"
            update.message.reply_html(text, disable_web_page_preview=True)

# Huobi


def send_profit36_messages(update, common_symbols63, ask_prices_binance, bid_prices_huobi):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits34 = []
    for symbol in common_symbols63:
        if symbol in ask_prices_binance:
            if ask_prices_binance[symbol] == 0:
                profit34 = 0
            else:
                profit34 = (
                    bid_prices_huobi[symbol] - ask_prices_binance[symbol]) / ask_prices_binance[symbol] * 100
        else:
            profit34 = 0
        profits34.append((symbol, profit34))
        # Сортировка списка по профиту в порядке убывания
    profits34.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit34 in profits34:
        if 0.5 <= profit34 <= 20:
            binance_url = f"https://www.binance.com/ru/trade/{symbol}"
            symbol1 = symbol.replace('USDT', '_USDT').lower()
            hyuobi_url = f"https://www.huobi.com/ru-ru/trade/{symbol1}?type=spot"
            base_symbol = re.split('USDC|USDT|ETH|BTC|TRY', symbol)[0]
            withdraw_fee = withdrawal_info[base_symbol]
            withdraw_fee = float(withdraw_fee) * \
                ask_prices_binance[symbol]
            text = f"{symbol}\n<a href='{binance_url}'>Покупка</a> на Binance = {ask_prices_binance[symbol]}\n<a href='{hyuobi_url}'>Продажа</a> на Huobi = {bid_prices_huobi[symbol]}\nСпред: {profit34:.2f}%\n\nРазмер комиссии: {withdraw_fee:.2f}"
            update.message.reply_html(
                text, disable_web_page_preview=True)
# Kucoin


def send_profit37_messages(update, common_symbols73, ask_prices_binance, bid_prices_kucoin1):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits34 = []
    for symbol in common_symbols73:
        if symbol in ask_prices_binance:
            if ask_prices_binance[symbol] == 0:
                profit34 = 0
            else:
                profit34 = (
                    bid_prices_kucoin1[symbol] - ask_prices_binance[symbol]) / ask_prices_binance[symbol] * 100
        else:
            profit34 = 0
        profits34.append((symbol, profit34))
        # Сортировка списка по профиту в порядке убывания
    profits34.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit34 in profits34:
        if 0.5 <= profit34 <= 20:
            binance_url = f"https://www.binance.com/ru/trade/{symbol}"
            symbol1 = symbol.replace(
                "USDT", "-USDT")
            kucoin_url = f"https://www.kucoin.com/ru/trade/{symbol1}"
            base_symbol = re.split('USDC|USDT|ETH|BTC|TRY', symbol)[0]
            withdraw_fee = withdrawal_info[base_symbol]
            withdraw_fee = float(withdraw_fee) * \
                ask_prices_binance[symbol]
            text = f"{symbol}\n<a href='{binance_url}'>Покупка</a> на Binance = {ask_prices_binance[symbol]}\n<a href='{kucoin_url}'>Продажа</a> на Kucoin = {bid_prices_kucoin1[symbol]}\nСпред: {profit34:.2f}%\n\nРазмер комиссии: {withdraw_fee:.2f}"
            update.message.reply_html(
                text, disable_web_page_preview=True)
