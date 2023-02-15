import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coinmarket.settings')

app = Celery('coinmarket')
app.config_from_object('django.conf:settings',namespace='CELERY')

app.conf.beat_schedule = {
    'get_coins_data_10s':{
        'task':'coins.tasks.get_coin_data',
        'schedule': 10.0 
    }
}


app.autodiscover_tasks()