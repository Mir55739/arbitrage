from pybit.unified_trading import HTTP
session = HTTP(
    testnet=True,
    api_key="XXXXX",
    api_secret="XXXXX",
)
print(session.get_coin_info(
    coin="ETH",
))