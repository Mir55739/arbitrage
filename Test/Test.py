import requests
symbol = 'CENX'


def calculate_profit(symbol):
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
            profit = bitmart_cost - mexc_revenue

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
    # Выводим информацию о лучшей комбинации ордеров
    if max_profit > 0:
        # Выводим информацию о лучшей комбинации ордеров
        print(
            f"Лучшая комбинация ордеров: покупка на Mexc (ордер {best_sell_order}), продажа на Bitmart (ордер {best_buy_order})")
        print(f"Объем покупки: {buy_volume_usdt} USDT")
        print(f"Объем продажи: {sell_volume_usdt} USDT")
        print(f"Средняя цена покупки: {mean_sell_price} USDT")
        print(f"Средняя цена продажи: {mean_buy_price} USDT")
        print(f"Максимальная прибыль: {max_profit:.2f} USDT")
    else:
        print("Нет комбинаций ордеров с положительной прибылью")

    return max_profit


calculate_profit(symbol)
