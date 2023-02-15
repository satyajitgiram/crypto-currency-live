from  asgiref.sync import async_to_sync
import requests
from django.forms.models import model_to_dict
from coins.models import coin
from celery import shared_task

from channels.layers import get_channel_layer

channel_layer = get_channel_layer()



@shared_task
def get_coin_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    COINS = []

    for coins in data:
        obj, created = coin.objects.get_or_create(symbol=coins['symbol'])
        obj.name =  coins['name']
        obj.symbol = coins['symbol']

        if obj.price < coins['current_price']:
            state = 'fall'
        elif obj.price == coins['current_price']:
            state = 'same'
        elif obj.price > coins['current_price']:
            state = 'raise'



        obj.price = coins['current_price']
        obj.rank = coins['market_cap_rank']
        obj.image = coins['image']


    
        obj.save()

        new_data = model_to_dict(obj)
        new_data.update({'state':state})

        COINS.append(new_data)
        
    async_to_sync(channel_layer.group_send)('coins',{'type':'send_new_data','text':COINS})
    