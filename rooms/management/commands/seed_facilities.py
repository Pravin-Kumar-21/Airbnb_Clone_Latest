from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "This Command Creates Facilities"

    def handle(self, *args, **options):
        facilities = [
            "Private Entrance",
            "Paid Parking on Premises ",
            "Paid Parking of Premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities Created"))
