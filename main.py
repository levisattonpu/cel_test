from services.tasks import get_results, app 
from data.coordinates import querydict



for i in querydict:
    data = get_results.delay(i)
    print(data)
    
print('RUNNING!!!\n'*10)

if __name__ == '__main__':
    args = ['worker', '--loglevel=INFO']
    app.worker_main(argv=args)


### Rodar Celery
# celery -A main worker -l INFO -E
### Rodar Flower
# celery -A main.app flower