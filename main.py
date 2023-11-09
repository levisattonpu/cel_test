from tasks import app, get_results
from data.coordinates import querydict

for location in querydict:
    get_results.delay(location)

print('RUNNING!!!\n'*10)

if __name__ == '__main__':
    args = ['-A', 'main','worker', '-l', 'INFO', '-E']
    app.worker_main(argv=args)
    # ['-A', 'main.app', 'flower']
    app.close()


### Rodar Celery
# celery -A main worker -l INFO -E
### Rodar Flower
# celery -A main.app flower