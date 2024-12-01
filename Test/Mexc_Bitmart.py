import requests
symbol = 'KOSON'


def calculate_profit(symbol):
    # Получаем стаканы котировок с двух бирж (Bitmart и Mexc)
    URL1 = f"https://api.mexc.com/api/v3/depth?symbol={symbol}USDT&limit=10"
    URL2 = f"https://api-cloud.bitmart.com/spot/v1/symbols/book?symbol={symbol}_USDT&depth=10"
    response1 = requests.get(URL1).json()
    response2 = requests.get(URL2).json()
    # print(response1)
    # print(response2)
    # Получаем информацию о лучшем спросе на Mexc
    ask_mexc = response1['asks']
    total_ask_mexc_volume = sum(float(x[1]) for x in ask_mexc)

    # Получаем информацию о лучшем предложении на Bitmart
    bid_bitmart = response2['data']['buys']
    total_bid_bitmart_volume = sum(float(x['amount']) for x in bid_bitmart)
    # Задаем желаемый объем торговли
    desired_trade_volume = 10000000

    # Находим лучшую цену продажи на Mexc
    best_ask_mexc = min(ask_mexc, key=lambda x: float(x[0]))

    # Находим лучшую цену покупки на Bitmart
    best_bid_bitmart = max(bid_bitmart, key=lambda x: float(x['price']))

    # Вычисляем максимальную прибыль
    max_profit = 0
    trade_volume = min(desired_trade_volume, float(
        best_bid_bitmart['amount']), float(best_ask_mexc[1]))
    while trade_volume > 0:
        if float(best_bid_bitmart['price']) > float(best_ask_mexc[0]):
            # Вычисляем прибыль для этой комбинации
            profit = (
                float(best_bid_bitmart['price']) - float(best_ask_mexc[0])) * trade_volume
            # Обновляем максимальную прибыль
            if profit > max_profit:
                max_profit = profit
                print(
                    f"Новая максимальная прибыль: {max_profit} (объем торговли: {trade_volume}, цена покупки: {best_ask_mexc[0]}, цена продажи: {best_bid_bitmart['price']})")

        # Уменьшаем объем торговли
        trade_volume -= 1

    print(f"Максимальная прибыль: {max_profit}")


calculate_profit(symbol)
