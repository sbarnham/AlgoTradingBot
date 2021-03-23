import alpaca_trade_api as tradeapi
import numpy as np
import time

global choice
choice = 1000

secret_key = '9CpzpKWOw0MBfUDGMPxSdFZFbeOFzeEmVfOYDr5w'
api_key = 'PKQX8J7UCYEBJ1YMGC0G'
endpoint = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(api_key, secret_key, endpoint, 'v2')

global account
account = api.get_account()

def getBuyingPower():
    print('${} is available as buying power.'.format(account.buying_power))

def listPositions():
    print(account.list_positions())

def getAssetTrades(asset):
    print(api.get_trades(asset, "2021-03-23", "2021-03-23", limit=5).df)

def bot():
    active_assets = api.list_assets(status='active')

def interface():
    global choice
    while choice != 0:
        #print(account)
        choice = input('''
                    Select 1 to find available buying power.
                    Select 2 to list all positions.
                    Select 3 to search most recent quote for a given stock.
                    Select Y to start up bot.
                    ''')
        if choice == '1':
            getBuyingPower()
        if choice == '2':
            listPositions()
        if choice == '3':
            asset = input('Enter desired stock by symbol ')
            getAssetKeyData(asset)

interface()