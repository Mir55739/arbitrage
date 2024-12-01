import bitget.spot.public_api as public

if __name__ == '__main__':
    api_key = "bg_061cc39012e230776beba6f38e99d851"
    secret_key = "f1d4a202120dd51cf9a4a0bfbbde1c02936d37e0fc1dfc49b064646f6242fc56"
    passphrase = "Tlupov07"  # Password


def get_withdrawal_info():
    api_key = "bg_061cc39012e230776beba6f38e99d851"
    secret_key = "f1d4a202120dd51cf9a4a0bfbbde1c02936d37e0fc1dfc49b064646f6242fc56"
    passphrase = "Tlupov07"  # Password
    publicApi = public.PublicApi(
        api_key, secret_key, passphrase, use_server_time=True, first=False)
    result = publicApi.currencies()
    withdraw = result['data']
    withdrawal_info = {}

    for token in withdraw:
        name = token['coinName']
        withdrawal_info[name] = []
        for chain in token['chains']:
            network = chain['chain']
            withdraw_true = chain['withdrawable']
            withdraw_fee = chain['withdrawFee']
            withdrawal_info[name].append(
                (network, withdraw_true, withdraw_fee))
    return withdrawal_info
