from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_nutrition_summary_email_task(to_email, subject, message):
    send_mail(subject, message, 'noreply@yourapp.com', [to_email])