import requests
symbol = 'PLCU'


def calculate_profit(symbol):
    # Получаем стаканы котировок с двух бирж (Bitmart и Mexc)
    URL1 = f"https://api.mexc.com/api/v3/depth?symbol={symbol}USDT&limit=10"
    URL2 = f"https://api-cloud.bitmart.com/spot/v1/symbols/book?symbol={symbol}_USDT&depth=10"
    response1 = requests.get(URL1).json()
    response2 = requests.get(URL2).json()
    # Получаем информацию о лучшем спросе на Bitmart
    ask_bitmart = response2['data']['sells']
    total_ask_bitmart_volume = sum(float(x['amount']) for x in ask_bitmart)

    # Получаем информацию о лучшем предложении на Mexc
    bid_mexc = response1['bids']
    total_bid_mexc_volume = sum(float(x[1]) for x in bid_mexc)

    # Рассчитываем прибыль с покупки на одной бирже и продажи на другой
    max_profit = 0
    max_buy_orders = 0
    max_sell_orders = 0
    max_buy_sum = 0
    max_sell_sum = 0
    max_buy_volume = 0
    max_sell_volume = 0
    for bid in bid_mexc:
        bid_price = float(bid[0])
        bid_volume = float(bid[1])
        profit = 0
        buy_orders = 0
        sell_orders = 0
        buy_sum = 0
        sell_sum = 0
        buy_volume = 0
        sell_volume = 0
        for ask in ask_bitmart:
            ask_price = float(ask['price'])
            ask_volume = float(ask['amount'])
            if bid_price > ask_price:
                volume = min(bid_volume, ask_volume)
                profit += volume * (bid_price - ask_price)
                buy_orders += 1
                sell_orders += 1
                buy_sum += volume * ask_price
                sell_sum += volume * bid_price
                buy_volume += volume
                sell_volume += volume
                bid_volume -= volume
                if bid_volume == 0:
                    break
        if profit > max_profit:
            max_profit = profit
            max_buy_orders = buy_orders
            max_sell_orders = sell_orders
            max_buy_sum = buy_sum
            max_sell_sum = sell_sum
            max_buy_volume = buy_volume
            max_sell_volume = sell_volume
    buy_avg_price = max_buy_sum / max_buy_volume if max_buy_volume > 0 else 0
    sell_avg_price = max_sell_sum / max_sell_volume if max_sell_volume > 0 else 0
    profit_percent = max_profit / max_buy_sum * 100 if max_buy_sum > 0 else 0
    return {
        'profit': max_profit,
        'buy_orders': max_buy_orders,
        'sell_orders': max_sell_orders,
        'buy_sum': max_buy_sum,
        'sell_sum': max_sell_sum,
        'buy_avg_price': buy_avg_price,
        'sell_avg_price': sell_avg_price,
        'profit_percent': profit_percent
    }


result = calculate_profit(symbol)
print(f"Profit: {result['profit']}")
print(f"Buy orders: {result['buy_orders']}")
print(f"Sell orders: {result['sell_orders']}")
print(f"Buy sum: {result['buy_sum']}")
print(f"Sell sum: {result['sell_sum']}")
print(f"Buy average price: {result['buy_avg_price']}")
print(f"Sell average price: {result['sell_avg_price']}")
print(f"Profit percent: {result['profit_percent']}%")