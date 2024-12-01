import requests
import re
from Huobi.WithdrawHuobi import get_withdrawal_fees


def get_ticker_data6():
    mexc = requests.get('https://api.huobi.pro/market/tickers')
    ticker_data6 = mexc.json()
    return ticker_data6


def get_prices_huobi(ticker_data6):
    ticker_all6 = ticker_data6['data']
    ask_prices_huobi = {ticker['symbol'].upper(): float(
        ticker['ask']) for ticker in ticker_all6}
    bid_prices_huobi = {ticker['symbol'].upper(): float(
        ticker['bid']) for ticker in ticker_all6}
    return ask_prices_huobi, bid_prices_huobi


ticker_data6 = get_ticker_data6()
get_prices_huobi(ticker_data6)

# Bitmart


def send_profit61_messages(update, common_symbols61, ask_prices_huobi, bid_prices_bitmart1):
    # Создание списка кортежей (символ, профит2)
    profits3 = []
    for symbol in common_symbols61:
        if symbol in ask_prices_huobi:
            if ask_prices_huobi[symbol] == 0:
                profit3 = 0
            else:
                profit3 = (
                    bid_prices_bitmart1[symbol] - ask_prices_huobi[symbol]) / ask_prices_huobi[symbol] * 100
        else:
            profit3 = 0
        profits3.append((symbol, profit3))
    # Сортировка списка по профиту в порядке убывания
    profits3.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit3 in profits3:
        if 0.5 <= profit3 <= 20:
            symbol1 = symbol.replace('USDT', '_USDT').lower()
            hyuobi_url = f"https://www.huobi.com/ru-ru/trade/{symbol1}?type=spot"
            bitmart_url = f"https://www.bitmart.com/trade/ru-RU?layout=basic&theme=dark&symbol={symbol}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            text = f"{symbol}\n<a href='{hyuobi_url}'>Покупка</a> на Huobi = {ask_prices_huobi[symbol]}\n<a href='{bitmart_url}'>Продажа</a> на Bitmart = {bid_prices_bitmart1[symbol]}\nСпред: {profit3:.2f}%"
            fees = get_withdrawal_fees(base_symbol)
            for chain, fee_info in fees.items():
                text += f"\nСеть вывода: {chain}"
                if fee_info["type"] == "fixed":
                    fee = fee_info["fee"]
                    price = ask_prices_huobi[symbol]
                    result = float(fee) * float(price)
                    text += f" \nКомиссия за вывод: {result:.2f}"
                elif fee_info["type"] == "rate":
                    text += f" \nWithdrawal Fee Rate: {fee_info['fee']}"
                else:
                    text += " \nNo withdrawal fee information available"

            update.message.reply_html(
                text, disable_web_page_preview=True)

# Mexc


def send_profit62_messages(update, common_symbols62, ask_prices_huobi, bid_prices_mexc1):
    # Создание списка кортежей (символ, профит2)
    profits3 = []
    for symbol in common_symbols62:
        if symbol in ask_prices_huobi:
            if ask_prices_huobi[symbol] == 0:
                profit3 = 0
            else:
                profit3 = (
                    bid_prices_mexc1[symbol] - ask_prices_huobi[symbol]) / ask_prices_huobi[symbol] * 100
        else:
            profit3 = 0
        profits3.append((symbol, profit3))
    # Сортировка списка по профиту в порядке убывания
    profits3.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit3 in profits3:
        if 0.5 <= profit3 <= 20:
            symbol1 = symbol.replace('USDT', '_USDT').lower()
            hyuobi_url = f"https://www.huobi.com/ru-ru/trade/{symbol1}?type=spot"
            mexc_url = f"https://www.mexc.com/ru-RU/exchange/{symbol1}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            text = f"{symbol}\n<a href='{hyuobi_url}'>Покупка</a> на Huobi = {ask_prices_huobi[symbol]}\n<a href='{mexc_url}'>Продажа</a> на Mexc = {bid_prices_mexc1[symbol]}\nСпред: {profit3:.2f}%"
            fees = get_withdrawal_fees(base_symbol)
            for chain, fee_info in fees.items():
                text += f"\nСеть вывода: {chain}"
                if fee_info["type"] == "fixed":
                    fee = fee_info["fee"]
                    price = ask_prices_huobi[symbol]
                    result = float(fee) * float(price)
                    text += f" \nКомиссия за вывод: {result:.2f}"
                elif fee_info["type"] == "rate":
                    text += f" \nWithdrawal Fee Rate: {fee_info['fee']}"
                else:
                    text += " \nNo withdrawal fee information available"

            update.message.reply_html(
                text, disable_web_page_preview=True)
# Binance


def send_profit63_messages(update, common_symbols63, ask_prices_huobi, bid_prices_binance):
    # Создание списка кортежей (символ, профит2)
    profits3 = []
    for symbol in common_symbols63:
        if symbol in ask_prices_huobi:
            if ask_prices_huobi[symbol] == 0:
                profit3 = 0
            else:
                profit3 = (
                    bid_prices_binance[symbol] - ask_prices_huobi[symbol]) / ask_prices_huobi[symbol] * 100
        else:
            profit3 = 0
        profits3.append((symbol, profit3))
    # Сортировка списка по профиту в порядке убывания
    profits3.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit3 in profits3:
        if 0.5 <= profit3 <= 20:
            symbol1 = symbol.replace('USDT', '_USDT').lower()
            hyuobi_url = f"https://www.huobi.com/ru-ru/trade/{symbol1}?type=spot"
            binance_url = f"https://www.binance.com/ru/trade/{symbol}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            text = f"{symbol}\n<a href='{hyuobi_url}'>Покупка</a> на Huobi = {ask_prices_huobi[symbol]}\n<a href='{binance_url}'>Продажа</a> на Binance = {bid_prices_binance[symbol]}\nСпред: {profit3:.2f}%"
            fees = get_withdrawal_fees(base_symbol)
            for chain, fee_info in fees.items():
                text += f"\nСеть вывода: {chain}"
                if fee_info["type"] == "fixed":
                    fee = fee_info["fee"]
                    price = ask_prices_huobi[symbol]
                    result = float(fee) * float(price)
                    text += f" \nКомиссия за вывод: {result:.2f}"
                elif fee_info["type"] == "rate":
                    text += f" \nWithdrawal Fee Rate: {fee_info['fee']}"
                else:
                    text += " \nNo withdrawal fee information available"

            update.message.reply_html(
                text, disable_web_page_preview=True)

# Bitget


def send_profit64_messages(update, common_symbols64, ask_prices_huobi, bid_prices_bitget):
    # Создание списка кортежей (символ, профит2)
    profits3 = []
    for symbol in common_symbols64:
        if symbol in ask_prices_huobi:
            if ask_prices_huobi[symbol] == 0:
                profit3 = 0
            else:
                profit3 = (
                    bid_prices_bitget[symbol] - ask_prices_huobi[symbol]) / ask_prices_huobi[symbol] * 100
        else:
            profit3 = 0
        profits3.append((symbol, profit3))
    # Сортировка списка по профиту в порядке убывания
    profits3.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit3 in profits3:
        if 0.5 <= profit3 <= 20:
            symbol1 = symbol.replace('USDT', '_USDT').lower()
            hyuobi_url = f"https://www.huobi.com/ru-ru/trade/{symbol1}?type=spot"
            bitget_url = f"https://www.bitget.com/ru/spot/{symbol}_SPBL?type=spot"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            text = f"{symbol}\n<a href='{hyuobi_url}'>Покупка</a> на Huobi = {ask_prices_huobi[symbol]}\n<a href='{bitget_url}'>Продажа</a> на Bitget = {bid_prices_bitget[symbol]}\nСпред: {profit3:.2f}%"
            fees = get_withdrawal_fees(base_symbol)
            for chain, fee_info in fees.items():
                text += f"\nСеть вывода: {chain}"
                if fee_info["type"] == "fixed":
                    fee = fee_info["fee"]
                    price = ask_prices_huobi[symbol]
                    result = float(fee) * float(price)
                    text += f" \nКомиссия за вывод: {result:.2f}"
                elif fee_info["type"] == "rate":
                    text += f" \nWithdrawal Fee Rate: {fee_info['fee']}"
                else:
                    text += " \nNo withdrawal fee information available"

            update.message.reply_html(
                text, disable_web_page_preview=True)
# Gate


def send_profit65_messages(update, common_symbols65, ask_prices_huobi, bid_prices_gate1):
    # Создание списка кортежей (символ, профит2)
    profits3 = []
    for symbol in common_symbols65:
        if symbol in ask_prices_huobi:
            if ask_prices_huobi[symbol] == 0 or not ask_prices_huobi[symbol] or not bid_prices_gate1[symbol]:
                profit3 = 0
            else:
                profit3 = (
                    bid_prices_gate1[symbol] - ask_prices_huobi[symbol]) / ask_prices_huobi[symbol] * 100
        else:
            profit3 = 0
        profits3.append((symbol, profit3))
    # Сортировка списка по профиту в порядке убывания
    profits3.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit3 in profits3:
        if 0.5 <= profit3 <= 20:
            symbol1 = symbol.replace('USDT', '_USDT').lower()
            hyuobi_url = f"https://www.huobi.com/ru-ru/trade/{symbol1}?type=spot"
            gate_url = f"https://www.gate.io/ru/trade/{symbol1}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            text = f"{symbol}\n<a href='{hyuobi_url}'>Покупка</a> на Huobi = {ask_prices_huobi[symbol]}\n<a href='{gate_url}'>Продажа</a> на Gate = {bid_prices_gate1[symbol]}\nСпред: {profit3:.2f}%"
            fees = get_withdrawal_fees(base_symbol)
            for chain, fee_info in fees.items():
                text += f"\nСеть вывода: {chain}"
                if fee_info["type"] == "fixed":
                    fee = fee_info["fee"]
                    price = ask_prices_huobi[symbol]
                    result = float(fee) * float(price)
                    text += f" \nКомиссия за вывод: {result:.2f}"
                elif fee_info["type"] == "rate":
                    text += f" \nWithdrawal Fee Rate: {fee_info['fee']}"
                else:
                    text += " \nNo withdrawal fee information available"

            update.message.reply_html(
                text, disable_web_page_preview=True)
# Kucoin


def send_profit67_messages(update, common_symbols76, ask_prices_huobi, bid_prices_kucoin1):
    # Создание списка кортежей (символ, профит2)
    profits3 = []
    for symbol in common_symbols76:
        if symbol in ask_prices_huobi:
            if ask_prices_huobi[symbol] == 0:
                profit3 = 0
            else:
                profit3 = (
                    bid_prices_kucoin1[symbol] - ask_prices_huobi[symbol]) / ask_prices_huobi[symbol] * 100
        else:
            profit3 = 0
        profits3.append((symbol, profit3))
    # Сортировка списка по профиту в порядке убывания
    profits3.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    for symbol, profit3 in profits3:
        if 0.5 <= profit3 <= 20:
            symbol1 = symbol.replace('USDT', '_USDT').lower()
            hyuobi_url = f"https://www.huobi.com/ru-ru/trade/{symbol1}?type=spot"
            symbol2 = symbol.replace(
                "USDT", "-USDT")
            kucoin_url = f"https://www.kucoin.com/ru/trade/{symbol2}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            text = f"{symbol}\n<a href='{hyuobi_url}'>Покупка</a> на Huobi = {ask_prices_huobi[symbol]}\n<a href='{kucoin_url}'>Продажа</a> на Kucoin = {bid_prices_kucoin1[symbol]}\nСпред: {profit3:.2f}%"
            fees = get_withdrawal_fees(base_symbol)
            for chain, fee_info in fees.items():
                text += f"\nСеть вывода: {chain}"
                if fee_info["type"] == "fixed":
                    fee = fee_info["fee"]
                    price = ask_prices_huobi[symbol]
                    result = float(fee) * float(price)
                    text += f" \nКомиссия за вывод: {result:.2f}"
                elif fee_info["type"] == "rate":
                    text += f" \nWithdrawal Fee Rate: {fee_info['fee']}"
                else:
                    text += " \nNo withdrawal fee information available"

            update.message.reply_html(
                text, disable_web_page_preview=True)
