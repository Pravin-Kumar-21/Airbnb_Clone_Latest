from django.shortcuts import render, redirect
from django.urls import reverse
from rooms import models as room_models
from . import models


def toggle_room(request, room_pk):
    room = room_models.Room.objects.get_or_none(pk=room_pk)
    action = request.GET.get("action", None)
    if room is not None and action is not None:
        the_list, _ = models.List.objects.get_or_create(
            user=request.user, name="My Favourites"
        )
        if action == "add":
            the_list.rooms.add(room)
        elif action == "remove":
            the_list.rooms.remove(room)
    return redirect(reverse("rooms:detail", kwargs={"pk": room_pk}))
