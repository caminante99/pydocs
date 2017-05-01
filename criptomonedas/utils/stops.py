# -*- coding: cp1252 -*-

from poloniex import poloniex
import config
from time import sleep

from database import Sesion

pol = poloniex.poloniex(config.pol_api_key, config.pol_api_secret)
TIMEOUT = 5


class Stop(object):
    def __init__(self, currency):
        self.currency = currency
    
    def sell_fixed(self, price, quantity):
        last_price = float(pol.returnTicker['BTC_' + self.currency]['last'])
        if last_price >= price:
            pol.sell('BTC_' + self.currency, price, quantity)
        else:
            sleep(TIMEOUT)

    def buy_fixed(self, price, quantity):
        last_price = float(pol.returnTicker['BTC_' + self.currency]['last'])
        if last_price <= price:
            pol.buy('BTC_' + self.currency, price, quantity)
        else:
            sleep(TIMEOUT)


Stop_loss('LTC').sell_fixed(0.1118, 80)
Stop_loss('LTC').buy_fixed(0.00662, 80)
    
