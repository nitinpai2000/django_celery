# Create your views here.
from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.decorators import api_view

from django_celery.tasks import send_email



# Create your views here.

@api_view(['GET'])

def getData(request):
    send_email.delay("nitin@sampleemail.com")
    return Response()