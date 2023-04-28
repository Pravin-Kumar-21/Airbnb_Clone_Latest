# Generated by Django 4.2 on 2023-04-28 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=140)),
                ("description", models.TextField()),
                ("country", django_countries.fields.CountryField(max_length=2)),
                ("city", models.CharField(max_length=80)),
                ("price", models.IntegerField()),
                ("address", models.CharField(max_length=140)),
                ("beds", models.IntegerField()),
                ("bedrooms", models.IntegerField()),
                ("baths", models.IntegerField()),
                ("check_in", models.TimeField()),
                ("check_out", models.TimeField()),
                ("instant_book", models.BooleanField(default=False)),
                (
                    "host",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
