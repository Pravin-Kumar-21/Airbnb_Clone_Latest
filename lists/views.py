from django.shortcuts import render, redirect
from django.urls import reverse
from rooms import models as room_models
from . import models


def save_room(request, room_pk):
    room = room_models.Room.objects.get_or_none(pk=room_pk)
    if room is not None:
        the_list, _ = models.List.objects.get_or_create(
            user=request.user, name="My Favourites"
        )
        the_list.rooms.add(room)
    return redirect(reverse("rooms:detail", kwargs={"pk": room_pk}))
