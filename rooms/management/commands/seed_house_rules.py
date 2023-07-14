from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):
    help = "This Command Creates House Rules"

    def handle(self, *args, **options):
        house_rules = [
            "No smoking",
            "No parties or events",
            "No pets",
            "Quiet hours",
            "Maximum occupancy",
            "Check-in and check-out times",
            "Respect for neighbors",
            "No unauthorized guests",
            "Keep the property clean",
            "Respect for property",
            "Lost or damaged items",
            "Use of utilities",
            "Safety and security",
            "Parking instructions",
            "Wi-Fi usage",
        ]
        for h in house_rules:
            HouseRule.objects.create(name=h)
        self.stdout.write(self.style.SUCCESS("House Rules  Created!"))
