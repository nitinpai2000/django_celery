# Celery settings
CELERY_IMPORTS = ("sampleapi.tasks", )
CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672/"
CELERY_RESULT_BACKEND = "rpc://"