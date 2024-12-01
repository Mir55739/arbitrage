import requests
from Book import calculate_average1, calculate_average2, calculate_average7
symbols = ['SOON', 'LFG', 'WMT']
const = 200
for symbol in symbols:
    # Получаем стаканы котировок с двух бирж (Bitmart и Mexc)
    ask_bitmart, bid_bitmart, volume_in_coins, step_usdt = calculate_average1(
        symbol, const)
    ask_mexc, bid_mexc, volume_in_coins, step_usdt = calculate_average2(
        symbol, const)
# ask_kucoin, bid_kucoin, volume_in_coins, step_usdt = calculate_average7(
#    symbol, const)


# mexc

    def calculate_average_price12(symbol, volume_in_coins, step_usdt):
        best_profit = 0
        best_ask_price = 0
        best_bid_price = 0
        best_ask_volume = 0
        best_bid_volume = 0
        best_ask_orders = 0
        best_bid_orders = 0
        step = step_usdt/float(ask_mexc[0][0])
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
                bid_price = float(bid["price"])
                bid_volume_in_coins = float(bid["amount"])
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
        print(f"\nЛучший вариант: покупка {best_ask_volume:.2f} USDT по средней цене {best_ask_price:.8f} ({best_ask_orders} ордеров) и продажа {best_bid_volume:.2f} USDT по средней цене {best_bid_price:.8f} ({best_bid_orders} ордеров). Прибыль: {best_profit:.2f} USDT")
        return best_ask_volume, best_ask_price, best_ask_orders, best_bid_volume, best_bid_price, best_bid_orders, best_profit
    calculate_average_price12(symbol, volume_in_coins, step_usdt)
