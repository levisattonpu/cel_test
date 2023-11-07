from celery import Celery
import os
from dotenv import load_dotenv
from worker import get_weather, querydict

BACKEND = os.getenv('BACKEND')
BROKER = os.getenv('BROKER')

app = Celery('tasks', backend=BACKEND, broker=BROKER)

@app.task
def get_results():
    weather_forecast_list = list(map(get_weather, querydict))
    return weather_forecast_list

data = get_results.delay()
print(data)

if __name__ == '__main__':
    args = ['worker', '--loglevel=INFO']
    app.worker_main(argv=args)