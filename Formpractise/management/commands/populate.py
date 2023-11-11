import json
import os.path
from Formpractise.models import Student
from django.core.management import BaseCommand

from Emobilisproject import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR,'dummydata.json')
        self.stdout.write(
            self.style.SUCCESS("Started importing data")
        )
        with open(path) as file:
            data = json.load(file)
            for i in data:
                Student.objects.create(
                    first_name=i['first_name'],
                    last_name=i['last_name'],
                    email_address=i['email_address'],
                    phone_number=i['phone_number'],
                    location=i['location'],
                    dateofBirth=i['dateofBirth']
                )

        self.stdout.write(
            self.style.SUCCESS("Finished importing data")
        )