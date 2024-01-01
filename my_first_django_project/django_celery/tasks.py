from time import sleep
from django_celery.celery import app

@app.task
def send_email(text):
        """Sends an email when the feedback form has been submitted."""
        sleep(20)  # Simulate expensive operation(s) that freeze Django
        return f"Sent email to {text}"
