# Register your models here.
from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Model"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guest",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "room_type",
    )
    list_filter = ("instant_book", "city", "country")
    search_fields = ("=city", "^host__username")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ """

    pass
