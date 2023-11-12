from Formpractise.models import Student
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = Student.objects.all()
        data.delete()
        self.stdout.write(
            self.style.SUCCESS("Deleted all data in database")
        )