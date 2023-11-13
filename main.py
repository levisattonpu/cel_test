import logging
from tasks import app, get_results
from data.coordinates import querydict

for location in querydict:
    get_results.delay(location)

logging.info('RUNNING!!!\n'*10)


### Rodar Celery
# celery -A main worker -l INFO -E
### Rodar Flower
# celery -A main.app flower