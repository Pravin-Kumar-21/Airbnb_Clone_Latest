from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django_countries import countries
from . import models


class HomeView(ListView):
    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):
    """Room Detail Definition"""

    model = models.Room


def search(request):
    city = request.GET.get("city")
    if city:
        city = str.capitalize(city)
    room_types = models.RoomType.objects.all()
    return render(
        request,
        "rooms/search.html",
        {"city": city, "countries": countries, "room_types": room_types},
    )
