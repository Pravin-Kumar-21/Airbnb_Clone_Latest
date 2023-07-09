from django.shortcuts import render
from . import models
import math


def all_rooms(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    page_count = models.Room.objects.count()
    page_count = math.ceil(page_count / page_size)
    all_rooms = models.Room.objects.all()[offset:limit]
    return render(
        request,
        "rooms/home.html",
        {
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1),
        },
    )
