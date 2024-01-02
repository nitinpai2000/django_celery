# Create your views here.
from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.decorators import api_view

from django_celery.tasks import send_email

from .celery import app as celery_app



# Create your views here.

@api_view(['GET'])

def getData(request):
    send_email.delay("nitin@sampleemail.com")
    return Response()

@api_view(['GET'])
def check_task_status(request, task_id):
    # Check the status of the Celery task    
    response = celery_app.AsyncResult(task_id)    
    return Response(response.state)