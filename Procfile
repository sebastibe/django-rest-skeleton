web: gunicorn -c gunicorn.py.ini api.wsgi:application
scheduler: python manage.py celery worker -B -E --maxtasksperchild=1000
worker: python manage.py celery worker -E --maxtasksperchild=1000