# django_celery/settings.py

# ...
CELERY_IMPORTS = ("django_celery.tasks", )
# Celery settings
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672/'
CELERY_RESULT_BACKEND = 'rpc://'