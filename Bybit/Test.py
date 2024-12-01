import requests
import cProfile

symbol = 'SHA'
const = 220

# Получаем стаканы котировок с двух бирж (Bitmart и Mexc)
URL1 = f"https://api.mexc.com/api/v3/depth?symbol={symbol}USDT&limit=10"
URL2 = f"https://api-cloud.bitmart.com/spot/v1/symbols/book?symbol={symbol}_USDT&depth=10"
URL3 = f"https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol={symbol}-USDT"
response1 = requests.get(URL1).json()
response2 = requests.get(URL2).json()
response3 = requests.get(URL3).json()

#ask_mexc = response1['asks']
ask_mexc = response3['data']['asks']
bid_bitmart = response2['data']['buys']
volume_in_coins = const/float(ask_mexc[0][0])
step_usdt = const/(const*10)
print(step_usdt)


def calculate_average_price(symbol, volume_in_coins, step_usdt):
    best_profit = 0
    best_ask_price = 0
    best_bid_price = 0
    best_ask_volume = 0
    best_bid_volume = 0
    best_ask_orders = 0
    best_bid_orders = 0
    step = step_usdt/float(ask_mexc[0][0])
    print(step)
    # Перебираем все варианты объема
    for v in range(int(volume_in_coins / step)):
        current_volume_in_coins = volume_in_coins - v * step
        # Рассчитываем среднюю цену покупки
        total_cost = 0
        total_volume = 0
        ask_orders = 0
        remaining_volume_in_coins = current_volume_in_coins
        for ask in ask_mexc:
            ask_price = float(ask[0])
            ask_volume_in_coins = float(ask[1])
            if remaining_volume_in_coins > 0:
                trade_volume_in_coins = min(
                    remaining_volume_in_coins, ask_volume_in_coins)
                total_cost += trade_volume_in_coins * ask_price
                total_volume += trade_volume_in_coins
                remaining_volume_in_coins -= trade_volume_in_coins
                ask_orders += 1
        average_ask_price = total_cost / total_volume

        # Рассчитываем среднюю цену продажи
        total_revenue = 0
        total_volume = 0
        bid_orders = 0
        remaining_volume_in_coins = current_volume_in_coins
        for bid in bid_bitmart:
            bid_price = float(bid['price'])
            bid_volume_in_coins = float(bid['amount'])
            if remaining_volume_in_coins > 0:
                trade_volume_in_coins = min(
                    remaining_volume_in_coins, bid_volume_in_coins)
                total_revenue += trade_volume_in_coins * bid_price
                total_volume += trade_volume_in_coins
                remaining_volume_in_coins -= trade_volume_in_coins
                bid_orders += 1
        average_bid_price = total_revenue / total_volume

        # Рассчитываем прибыль в USDT
        profit_in_USDT = (average_bid_price -
                          average_ask_price) * current_volume_in_coins

        if profit_in_USDT > best_profit:
            best_profit = profit_in_USDT
            best_ask_price = average_ask_price
            best_bid_price = average_bid_price
            best_ask_volume = current_volume_in_coins * \
                average_ask_price  # Конвертируем объем из монет в USDT
            best_bid_volume = current_volume_in_coins * \
                average_bid_price  # Конвертируем объем из монет в USDT
            best_ask_orders = ask_orders
            best_bid_orders = bid_orders

    print(f"Лучший вариант: покупка {best_ask_volume:.2f} USDT по средней цене {best_ask_price:.6f} ({best_ask_orders} ордеров) и продажа {best_bid_volume:.2f} USDT по средней цене {best_bid_price:.6f} ({best_bid_orders} ордеров). Прибыль: {best_profit:.2f} USDT")


calculate_average_price(symbol, volume_in_coins, step_usdt)
# Пример использования функции
#cProfile.run('calculate_average_price(symbol, volume_in_coins, step_usdt)')


'''
def calculate_average_price(symbol, volume_in_coins, step):
    best_profit = 0
    best_ask_price = 0
    best_bid_price = 0
    best_ask_volume = 0
    best_bid_volume = 0
    best_ask_orders = 0
    best_bid_orders = 0

    # Перебираем все варианты объема
    for v in range(int(volume_in_coins / step)):
        current_volume_in_coins = volume_in_coins - v * step
        # Рассчитываем среднюю цену покупки
        total_cost = 0
        total_volume = 0
        ask_orders = 0
        remaining_volume_in_coins = current_volume_in_coins

        min_ask_volume_in_coins = min([float(ask[1]) for ask in ask_mexc])

        for ask in ask_mexc:
            ask_price = float(ask[0])
            ask_volume_in_coins = float(ask[1])
            if remaining_volume_in_coins > 0:
                trade_volume_in_coins = min(
                    remaining_volume_in_coins, min_ask_volume_in_coins)
                total_cost += trade_volume_in_coins * ask_price
                total_volume += trade_volume_in_coins
                remaining_volume_in_coins -= trade_volume_in_coins
                ask_orders += 1
        average_ask_price = total_cost / total_volume

        # Рассчитываем среднюю цену продажи
        total_revenue = 0
        total_volume = 0
        bid_orders = 0
        remaining_volume_in_coins = current_volume_in_coins

        min_bid_volume_in_coins = min(
            [float(bid['amount']) for bid in bid_bitmart])

        for bid in bid_bitmart:
            bid_price = float(bid['price'])
            bid_volume_in_coins = float(bid['amount'])
            if remaining_volume_in_coins > 0:
                trade_volume_in_coins = min(
                    remaining_volume_in_coins, min_bid_volume_in_coins)
                total_revenue += trade_volume_in_coins * bid_price
                total_volume += trade_volume_in_coins
                remaining_volume_in_coins -= trade_volume_in_coins
                bid_orders += 1
        average_bid_price = total_revenue / total_volume

        # Рассчитываем прибыль в USDT
        profit_in_USDT = (average_bid_price -
                          average_ask_price) * current_volume_in_coins

        if profit_in_USDT > best_profit:
            best_profit = profit_in_USDT
            best_ask_price = average_ask_price
            best_bid_price = average_bid_price
            best_ask_volume = current_volume_in_coins * \
                average_ask_price  # Конвертируем объем из монет в USDT
            best_bid_volume = current_volume_in_coins * \
                average_bid_price  # Конвертируем объем из монет в USDT
            best_ask_orders = ask_orders
            best_bid_orders = bid_orders

    print(f"Лучший вариант: покупка {best_ask_volume:.2f} USDT по средней цене {best_ask_price:.6f} ({best_ask_orders} ордеров) и продажа {best_bid_volume:.2f} USDT по средней цене {best_bid_price:.6f} ({best_bid_orders} ордеров). Прибыль: {best_profit:.2f} USDT")


# Пример использования функции
cProfile.run('calculate_average_price(symbol, volume_in_coins, step)')'''
