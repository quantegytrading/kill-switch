# kill-switch.py

import os
import ccxt
from ccxt import InvalidOrder, InsufficientFunds


def init_exchange():
    exchange_class = getattr(ccxt, 'binanceus')
    exchange = exchange_class({
        'apiKey': os.environ['key'],
        'secret': os.environ['secret'],
        'timeout': 30000,
        'enableRateLimit': True,
    })
    exchange.loadMarkets()
    return exchange


def truncate_float(f) -> float:
    ff = format(f, '.10f')
    s = str(ff)
    xs = s.split('.')
    return float(xs[0] + '.' + xs[1][:6])


def main(event, context):
    base_currency = 'USD'

    exchange = init_exchange()
    symbols = exchange.fetchBalance()
    for symbol in symbols.get('free'):
        if symbol not in [base_currency]:
            free = truncate_float(symbols.get(symbol).get('free'))
            if free > 0:
                print(symbol + ": " + str(free))
                try:
                    # order = exchange.createMarketSellOrder(symbol + '/' + base_currency, free)
                    print("Sell:")
                    print(order)
                except InvalidOrder as e:
                    print(e)
                except InsufficientFunds as e:
                    print(e)


if __name__ == "__main__":
    main('', '')