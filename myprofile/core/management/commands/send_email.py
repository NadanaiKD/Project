from django.core.management.base import BaseCommand, CommandError
from django.core.mail import get_connection, send_mail
# from polls.models import Question as Poll
from core.models import Email


class Command(BaseCommand):
    help = 'Send email to every emails in database'

    def handle(self, *args, **options):
        print(args)
        print(options)

        try:
            emails = Email.objects.all()
            for email in emails:
                print(email.email)
                with get_connection():
                    send_mail(
                        'Thankyou for subscriber me',
                        'I am so excited for welcome you',
                        'Thank you again',
                        [email.email],
                    )
        except Exception:
            raise CommandError("Error!")
