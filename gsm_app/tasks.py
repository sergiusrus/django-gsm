from background_task import background
from django.core.mail import send_mail


@background(schedule=10)
def send_email_from_put():
    send_mail(
        'Subject of email',
        'The message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
