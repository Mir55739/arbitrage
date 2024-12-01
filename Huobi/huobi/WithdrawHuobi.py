from huobi.constant.test import g_api_key, g_secret_key
from huobi.client.etf import EtfClient
from huobi.client.generic import GenericClient
import time

from huobi.client.margin import MarginClient
from huobi.client.trade import TradeClient
from huobi.client.wallet import WalletClient
from huobi.constant import *
from performance.account_performance import AccountClientPerformance
from performance.market_performance import MarketClientPerformance


class RunStatus:
    SUCCESS = "OK"
    FAILED = "Fail"


ROUND_SIZE = 3
TRANSFER_TRX_MIN_AMOUNT = 100

time_cost_detail_list = []
count_offset = 0

# prepare list
withdraw_address = "TRec1vonZcbcXHs5TZLuH2WTa8ejXvnTm8"
loan_amount = 100
loan_currency = "usdt"
loan_symbol = "eosusdt"
trade_symbol = "eosusdt"


class TimeCost:
    sdk_api_start_time = 0.0  # SDK call start time
    # time cost from response.elapsed.total_seconds(), cost is from sending request to receive response
    server_req_cost = 0.0
    # manually statistics time before/after requests.get  (server_api_cost >= server_req_cost)
    server_api_cost = 0.0
    function_name = ""
    run_status = ""

    def __init__(self, function_name=""):
        self.sdk_api_start_time = round(time.time(), ROUND_SIZE + 1)
        self.function_name = function_name


wallet_client = WalletClient(
    api_key=g_api_key, secret_key=g_secret_key, performance_test=True)

tc = TimeCost(function_name=wallet_client.get_account_withdraw_quota.__name__)
result, tc.server_req_cost, tc.server_api_cost = wallet_client.get_account_withdraw_quota(
    currency="usdt")
tc.run_status = RunStatus.SUCCESS if result and len(
    result) else RunStatus.FAILED
tc.add_record()
