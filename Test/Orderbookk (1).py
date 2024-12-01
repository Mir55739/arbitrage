import requests
symbol = 'OPTIMUS'


def calculate_profit(symbol):
    # Получаем стаканы котировок с двух бирж (Bitmart и Mexc)
    URL1 = f"https://api-cloud.bitmart.com/spot/v1/symbols/book?symbol={symbol}_USDT&depth=5"
    URL2 = f"https://api.mexc.com/api/v3/depth?symbol={symbol}USDT&limit=5"
    response1 = requests.get(URL1).json()
    response2 = requests.get(URL2).json()
    # Получаем информацию о лучшем спросе на Mex
    ask_mexc = response2['asks']
    total_ask_mexc_volume = sum(float(x[1]) for x in ask_mexc)
    print(ask_mexc)

    # Получаем информацию о лучшем предложении на Bitmart
    bid_bitmart = response1['data']['buys']
    total_bid_bitmart_volume = sum(float(x['amount']) for x in bid_bitmart)

    # Считаем прибыль для каждой комбинации ордеров
    max_profit = 0
    buy_amounts = []
    sell_amounts = []
    for i in range(1, 6):  # Bitmart buy
        bitmart_price = float(bid_bitmart[i-1]['price'])
        bitmart_volume = float(bid_bitmart[i-1]['amount'])

        # Рассчитываем сумму покупки
        bitmart_amount = bitmart_price * bitmart_volume
        buy_amounts.append(bitmart_amount)
        for j in range(1, 6):  # Mexc sell
            mexc_price = float(ask_mexc[j-1][0])
            mexc_volume = float(ask_mexc[j-1][1])
            # Вычисляем объем продажи
            sell_volume = min(
                [bitmart_volume, mexc_volume, total_ask_mexc_volume])

            # Рассчитываем стоимость покупки на Bitmart и продажи на Mexc
            bitmart_cost = sell_volume * bitmart_price
            mexc_revenue = sell_volume * mexc_price

            # Рассчитываем сумму продажи
            mexc_amount = mexc_revenue
            sell_amounts.append(mexc_amount)
            print(sell_amounts)
            # Рассчитываем прибыль
            profit = mexc_revenue - bitmart_cost

            # Обновляем максимальную прибыль
            if profit > max_profit:
                max_profit = profit

            # Уменьшаем объемы в соответствии с продажей
            bitmart_volume -= sell_volume
            mexc_volume -= sell_volume
            total_ask_mexc_volume -= sell_volume

            # Выходим из цикла, если объемы продажи достигли нуля
            if bitmart_volume == 0 or mexc_volume == 0 or total_ask_mexc_volume == 0:
                break

    # Рассчитываем среднюю цену покупки
    mean_buy_price = sum(buy_amounts) / \
        sum(float(x['amount']) for x in bid_bitmart)

    # Получаем количество ордеров на покупку
    num_buy_orders = len(bid_bitmart)

    # Получаем общую сумму покупки
    total_buy_amount = sum(buy_amounts)

    # Рассчитываем среднюю цену продажи
    mean_sell_price = sum(sell_amounts) / sum(float(x[1]) for x in ask_mexc)

    # Получаем количество ордеров на продажу
    num_sell_orders = len(ask_mexc)

    # Получаем общую сумму продажи
    total_sell_amount = sum(sell_amounts)

    # Рассчитываем процент прибыли
    profit_percent = (max_profit / total_buy_amount) * 100

    # Выводим информацию
    print(f"Средняя цена покупки: {mean_buy_price:.2f} USDT")
    print(f"Количество ордеров на покупку: {num_buy_orders}")
    print(f"Общая сумма покупки: {total_buy_amount:.2f} USDT")
    print(f"Средняя цена продажи: {mean_sell_price:.2f} USDT")
    print(f"Количество ордеров на продажу: {num_sell_orders}")
    print(f"Общая сумма продажи: {total_sell_amount:.2f} USDT")
    print(f"Процент прибыли: {profit_percent:.2f}%")

    return max_profit


calculate_profit(symbol)
