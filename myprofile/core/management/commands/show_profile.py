from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll
from core.models import Profile


class Command(BaseCommand):
    help = 'This is a command to show my profile'

    def add_arguments(self, parser):
        parser.add_argument('id', nargs='1', type=int)
        parser.add_argument('name', narge=1, type=str)

    def handle(self, *args, **options):
        print(args)
        print(options)

        try:
            id = options.get("id")[0]
            print(id)
            profile = Profile.objects.get(id=id)
            print(profile.name)
            print(profile.short_bio)
        except Exception:
            raise CommandError("Error!")