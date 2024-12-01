import re
import bitget.spot.market_api as market
from WithdrawBitget import get_withdrawal_info

bitget_buy_enabled = True
bitget_sell_enabled = True
if __name__ == '__main__':
    api_key = "bg_061cc39012e230776beba6f38e99d851"
    secret_key = "f1d4a202120dd51cf9a4a0bfbbde1c02936d37e0fc1dfc49b064646f6242fc56"
    passphrase = "Tlupov07"  # Password


def get_ticker_data43():
    api_key = "bg_061cc39012e230776beba6f38e99d851"
    secret_key = "f1d4a202120dd51cf9a4a0bfbbde1c02936d37e0fc1dfc49b064646f6242fc56"
    passphrase = "Tlupov07"  # Password
    marketApi = market.MarketApi(
        api_key, secret_key, passphrase, use_server_time=False, first=False)
    result = marketApi.tickers()
    ticker_data43 = result['data']
    return ticker_data43


def get_prices_bitget(ticker_data43):
    ask_prices_bitget = {ticker['symbol']:
                         float(ticker['sellOne']) for ticker in ticker_data43}
    bid_prices_bitget = {ticker['symbol']:
                         float(ticker['buyOne']) for ticker in ticker_data43}
    return ask_prices_bitget, bid_prices_bitget

# ////////////////////////////////////////////////////////////
# bitmart


def send_profit41_messages(update, common_symbols41, ask_prices_bitget, bid_prices_bitmart1):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits41 = []
    for symbol in common_symbols41:
        if symbol in ask_prices_bitget:
            if ask_prices_bitget[symbol] == 0:
                profit41 = 0
            else:
                profit41 = (
                    bid_prices_bitmart1[symbol] - ask_prices_bitget[symbol]) / ask_prices_bitget[symbol] * 100
        else:
            profit41 = 0
        profits41.append((symbol, profit41))
        # Сортировка списка по профиту в порядке убывания
    profits41.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    withdrawal_info = get_withdrawal_info()
    for symbol, profit41 in profits41:
        if 0.5 <= profit41 <= 20:
            bitget_url = f"https://www.bitget.com/ru/spot/{symbol}_SPBL?type=spot"
            symbol1 = symbol.replace(
                "USDT", "_USDT")
            bitmart_url = f"https://www.bitmart.com/trade/ru-RU?layout=basic&theme=dark&symbol={symbol1}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            text = f"{symbol}\n<a href='{bitget_url}'>Покупка</a> на Bitget = {ask_prices_bitget[symbol]}\n<a href='{bitmart_url}'>Продажа</a> на Bitmart = {bid_prices_bitmart1[symbol]}\nСпред: {profit41:.2f}%"
            for network_info in withdrawal_info[base_symbol]:
                network, withdraw_true, withdraw_fee = network_info
                withdraw_fee = float(withdraw_fee) * \
                    ask_prices_bitget[symbol]
                text += f"\n\nСеть вывода: {network}\nСтатус вывода: {withdraw_true}\nРазмер комиссии: {withdraw_fee:.2f}"
            update.message.reply_html(
                text, disable_web_page_preview=True)

# Mexc


def send_profit42_messages(update, common_symbols24, ask_prices_bitget, bid_prices_mexc1):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits42 = []
    for symbol in common_symbols24:
        if symbol in ask_prices_bitget:
            if ask_prices_bitget[symbol] == 0:
                profit42 = 0
            else:
                profit42 = (
                    bid_prices_mexc1[symbol] - ask_prices_bitget[symbol]) / ask_prices_bitget[symbol] * 100
        else:
            profit42 = 0
        profits42.append((symbol, profit42))
        # Сортировка списка по профиту в порядке убывания
    profits42.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    withdrawal_info = get_withdrawal_info()
    for symbol, profit42 in profits42:
        if 0.5 <= profit42 <= 20:
            bitget_url = f"https://www.bitget.com/ru/spot/{symbol}_SPBL?type=spot"
            mexc_url = f"https://www.mexc.com/ru-RU/exchange/{symbol}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            text = f"{symbol}\n<a href='{bitget_url}'>Покупка</a> на Bitget = {ask_prices_bitget[symbol]}\n<a href='{mexc_url}'>Продажа</a> на Mexc = {bid_prices_mexc1[symbol]}\nСпред: {profit42:.2f}%"
            for network_info in withdrawal_info[base_symbol]:
                network, withdraw_true, withdraw_fee = network_info
                withdraw_fee = float(withdraw_fee) * \
                    ask_prices_bitget[symbol]
                text += f"\n\nСеть вывода: {network}\nСтатус вывода: {withdraw_true}\nРазмер комиссии: {withdraw_fee:.2f}"
            update.message.reply_html(
                text, disable_web_page_preview=True)

# Binance


def send_profit43_messages(update, common_symbols34, ask_prices_bitget, bid_prices_binance):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits43 = []
    for symbol in common_symbols34:
        if symbol in ask_prices_bitget:
            if ask_prices_bitget[symbol] == 0:
                profit43 = 0
            else:
                profit43 = (
                    bid_prices_binance[symbol] - ask_prices_bitget[symbol]) / ask_prices_bitget[symbol] * 100
        else:
            profit43 = 0
        profits43.append((symbol, profit43))
        # Сортировка списка по профиту в порядке убывания
    profits43.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    withdrawal_info = get_withdrawal_info()
    for symbol, profit43 in profits43:
        if 0.5 <= profit43 <= 20:
            bitget_url = f"https://www.bitget.com/ru/spot/{symbol}_SPBL?type=spot"
            binance_url = f"https://www.binance.com/ru/trade/{symbol}"
            base_symbol = re.split('USDC|USDT|ETH|BTC|EUR', symbol)[0]
            text = f"{symbol}\n<a href='{bitget_url}'>Покупка</a> на Bitget = {ask_prices_bitget[symbol]}\n<a href='{binance_url}'>Продажа</a> на Binance = {bid_prices_binance[symbol]}\nСпред: {profit43:.2f}%"
            if base_symbol in withdrawal_info:
                for network_info in withdrawal_info[base_symbol]:
                    network, withdraw_true, withdraw_fee = network_info
                    withdraw_fee = float(withdraw_fee) * \
                        ask_prices_bitget[symbol]
                    text += f"\n\nСеть вывода: {network}\nСтатус вывода: {withdraw_true}\nРазмер комиссии: {withdraw_fee:.2f}"
            else:
                # Обработка случая отсутствия ключа
                pass

            update.message.reply_html(
                text, disable_web_page_preview=True)

# Gate


def send_profit45_messages(update, common_symbols54, ask_prices_bitget, bid_prices_gate1):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits41 = []
    for symbol in common_symbols54:
        if symbol in ask_prices_bitget:
            if ask_prices_bitget[symbol] == 0 or not ask_prices_bitget[symbol] or not bid_prices_gate1[symbol]:
                profit41 = 0
            else:
                profit41 = (
                    bid_prices_gate1[symbol] - ask_prices_bitget[symbol]) / ask_prices_bitget[symbol] * 100
        else:
            profit41 = 0
        profits41.append((symbol, profit41))
        # Сортировка списка по профиту в порядке убывания
    profits41.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    withdrawal_info = get_withdrawal_info()
    for symbol, profit41 in profits41:
        if 0.5 <= profit41 <= 20:
            symbol1 = symbol.replace(
                "USDT", "_USDT")
            bitget_url = f"https://www.bitget.com/ru/spot/{symbol}_SPBL?type=spot"
            gate_url = f"https://www.gate.io/ru/trade/{symbol1}"
            base_symbol = re.split('USDC|USDT|ETH|BTC', symbol)[0]
            text = f"{symbol}\n<a href='{bitget_url}'>Покупка</a> на Bitget = {ask_prices_bitget[symbol]}\n<a href='{gate_url}'>Продажа</a> на Gate = {bid_prices_gate1[symbol]}\nСпред: {profit41:.2f}%"
            for network_info in withdrawal_info[base_symbol]:
                network, withdraw_true, withdraw_fee = network_info
                withdraw_fee = float(withdraw_fee) * \
                    ask_prices_bitget[symbol]
                text += f"\n\nСеть вывода: {network}\nСтатус вывода: {withdraw_true}\nРазмер комиссии: {withdraw_fee:.2f}"
            update.message.reply_html(
                text, disable_web_page_preview=True)

# Huobi


def send_profit46_messages(update, common_symbols64, ask_prices_bitget, bid_prices_huobi):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits43 = []
    for symbol in common_symbols64:
        if symbol in ask_prices_bitget:
            if ask_prices_bitget[symbol] == 0:
                profit43 = 0
            else:
                profit43 = (
                    bid_prices_huobi[symbol] - ask_prices_bitget[symbol]) / ask_prices_bitget[symbol] * 100
        else:
            profit43 = 0
        profits43.append((symbol, profit43))
        # Сортировка списка по профиту в порядке убывания
    profits43.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    withdrawal_info = get_withdrawal_info()
    for symbol, profit43 in profits43:
        if 0.5 <= profit43 <= 20:
            bitget_url = f"https://www.bitget.com/ru/spot/{symbol}_SPBL?type=spot"
            symbol1 = symbol.replace('USDT', '_USDT').lower()
            hyuobi_url = f"https://www.huobi.com/ru-ru/trade/{symbol1}?type=spot"
            base_symbol = re.split('USDC|USDT|ETH|BTC|EUR', symbol)[0]
            text = f"{symbol}\n<a href='{bitget_url}'>Покупка</a> на Bitget = {ask_prices_bitget[symbol]}\n<a href='{hyuobi_url}'>Продажа</a> на Huobi = {bid_prices_huobi[symbol]}\nСпред: {profit43:.2f}%"
            if base_symbol in withdrawal_info:
                for network_info in withdrawal_info[base_symbol]:
                    network, withdraw_true, withdraw_fee = network_info
                    withdraw_fee = float(withdraw_fee) * \
                        ask_prices_bitget[symbol]
                    text += f"\n\nСеть вывода: {network}\nСтатус вывода: {withdraw_true}\nРазмер комиссии: {withdraw_fee:.2f}"
            else:
                # Обработка случая отсутствия ключа
                pass

            update.message.reply_html(
                text, disable_web_page_preview=True)
# Kucoin


def send_profit47_messages(update, common_symbols74, ask_prices_bitget, bid_prices_kucoin1):
    withdrawal_info = get_withdrawal_info()
    # Создание списка кортежей (символ, профит2)
    profits43 = []
    for symbol in common_symbols74:
        if symbol in ask_prices_bitget:
            if ask_prices_bitget[symbol] == 0:
                profit43 = 0
            else:
                profit43 = (
                    bid_prices_kucoin1[symbol] - ask_prices_bitget[symbol]) / ask_prices_bitget[symbol] * 100
        else:
            profit43 = 0
        profits43.append((symbol, profit43))
        # Сортировка списка по профиту в порядке убывания
    profits43.sort(key=lambda x: x[1], reverse=True)
    # Отправка сообщений для второго условия в отсортированном порядке
    withdrawal_info = get_withdrawal_info()
    for symbol, profit43 in profits43:
        if 0.5 <= profit43 <= 20:
            bitget_url = f"https://www.bitget.com/ru/spot/{symbol}_SPBL?type=spot"
            symbol2 = symbol.replace(
                "USDT", "-USDT")
            kucoin_url = f"https://www.kucoin.com/ru/trade/{symbol2}"
            base_symbol = re.split('USDC|USDT|ETH|BTC|EUR', symbol)[0]
            text = f"{symbol}\n<a href='{bitget_url}'>Покупка</a> на Bitget = {ask_prices_bitget[symbol]}\n<a href='{kucoin_url}'>Продажа</a> на Kucoin = {bid_prices_kucoin1[symbol]}\nСпред: {profit43:.2f}%"
            if base_symbol in withdrawal_info:
                for network_info in withdrawal_info[base_symbol]:
                    network, withdraw_true, withdraw_fee = network_info
                    withdraw_fee = float(withdraw_fee) * \
                        ask_prices_bitget[symbol]
                    text += f"\n\nСеть вывода: {network}\nСтатус вывода: {withdraw_true}\nРазмер комиссии: {withdraw_fee:.2f}"
            else:
                # Обработка случая отсутствия ключа
                pass

            update.message.reply_html(
                text, disable_web_page_preview=True)
