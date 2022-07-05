import requests
import time

api_key = '****************************'
bot_key = '*********************************************'
chat_id = '***************'
limit = 41000
time_interval = 1 * 60

def get_price():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',
        'limit':'5000',
        'convert':'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
    }

    response = requests.get(url, headers=headers, params=parameters).json()
    bitcoin_price = response['data'][0]['quote']['USD']['price']
    return bitcoin_price

def send_update(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)

def main():
    while True:
        price = get_price()
        if (price < limit):
            send_update(chat_id, f"stronk saying bitcoin price has changed: {price}")
        else:
            send_update(chat_id, f"maw9e3 walo: {price}")
        time.sleep(time_interval)

main()
