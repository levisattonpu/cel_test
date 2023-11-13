from celery import Celery
from celery.schedules import crontab
import time
import os
from dotenv import load_dotenv

load_dotenv()

app = Celery('tasks', backend=os.getenv('BACKEND'), broker=os.getenv('BROKER'))

@app.task
def add(x, y):
    time.sleep(5)
    return x + y

# Define a periodic task
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': crontab(minute='*/1'),
        'args': (4, 4),
    },
}

app.conf.timezone = 'UTC'
