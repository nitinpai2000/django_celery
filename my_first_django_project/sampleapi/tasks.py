from time import sleep
from django.core.mail import send_mail
from celery import shared_task
from sampleapi.celery import app

@app.task
def send_feedback_email_task(text):
    sleep(20)
    return f"Email sent to {text}"