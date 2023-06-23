# Generated by Django 4.2 on 2023-06-23 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0007_alter_room_host"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="amenities",
            field=models.ManyToManyField(
                blank=True, related_name="rooms", to="rooms.amenity"
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="facilities",
            field=models.ManyToManyField(
                blank=True, related_name="rooms", to="rooms.facility"
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="house_rules",
            field=models.ManyToManyField(
                blank=True, related_name="rooms", to="rooms.houserule"
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="room_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="rooms",
                to="rooms.roomtype",
            ),
        ),
    ]
