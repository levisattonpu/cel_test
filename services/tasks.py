from celery import Celery
import os
from dotenv import load_dotenv
from services.worker import get_weather

load_dotenv()

app = Celery('tasks', backend=os.getenv('BACKEND'), broker=os.getenv('BROKER'))

@app.task
def get_results(querydict):
    weather_forecast_list = get_weather(querydict)
    return weather_forecast_list

