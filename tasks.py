from celery import Celery
import os
from dotenv import load_dotenv
from services.worker import get_weather
from datetime import timedelta

load_dotenv()

app = Celery('tasks', backend=os.getenv('BACKEND'), broker=os.getenv('BROKER'))

app.conf.update(
    CELERYBEAT_SCHEDULE={
        'perminute': {
            'task': 'tasks.get_results',
            'schedule': timedelta(seconds=3),
            'args': (1, 1)
        }
    }
)

@app.task
def get_results(location:dict):
    weather_forecast_list = get_weather(location)
    return weather_forecast_list
