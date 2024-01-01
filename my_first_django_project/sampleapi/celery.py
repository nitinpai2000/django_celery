import os
from celery import Celery
from django.apps import apps

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sampleapi.settings")
app = Celery("sampleapi")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()