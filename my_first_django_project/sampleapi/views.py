# Create your views here.
from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.decorators import api_view

from sampleapi.tasks import send_feedback_email_task



# Create your views here.

@api_view(['GET'])

def getData(request):

    send_feedback_email_task.delay("nitinpai@someexample.com")
    return Response()