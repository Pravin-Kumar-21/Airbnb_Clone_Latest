from django.db import models


# Create your models here.
class TimeStamped(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
