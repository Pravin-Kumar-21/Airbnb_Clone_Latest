# Generated by Django 4.2.5 on 2023-09-23 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("reservations", "0003_alter_reservation_guest_alter_reservation_room"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookedDay",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("day", models.DateField()),
                (
                    "reservation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reservations.reservation",
                    ),
                ),
            ],
            options={
                "verbose_name": "Booked Day",
                "verbose_name_plural": "Booked Days",
            },
        ),
    ]