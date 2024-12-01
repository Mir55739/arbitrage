from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
gate_buy_enabled = True
gate_sell_enabled = True
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host="https://api.gateio.ws/api/v4"
)


def get_ticker_data5():
    api_client = gate_api.ApiClient(configuration)
    # Create an instance of the API class
    api_instance = gate_api.SpotApi(api_client)
    timezone = 'utc0'
    # Retrieve ticker information
    ticker_data5 = api_instance.list_tickers(timezone=timezone)
    return ticker_data5


def get_prices_gate(ticker_data5):
    ticker_all2 = ticker_data5
    ask_prices_gate = {ticker.currency_pair:
                       ticker.lowest_ask for ticker in ticker_all2}
    bid_prices_gate = {ticker.currency_pair:
                       ticker.highest_bid for ticker in ticker_all2}
    for key in ask_prices_gate:
        if ask_prices_gate[key]:
            ask_prices_gate[key] = float(ask_prices_gate[key])
        else:
            # Пропуск пустой строки
            continue
    for key in bid_prices_gate:
        if bid_prices_gate[key]:
            bid_prices_gate[key] = float(bid_prices_gate[key])
        else:
            # Пропуск пустой строки
            continue
    return ask_prices_gate, bid_prices_gate


ticker_data5 = get_ticker_data5()
get_prices_gate(ticker_data5)
