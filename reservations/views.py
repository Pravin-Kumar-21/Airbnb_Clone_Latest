import datetime
from django.views.generic import View
from rooms import models as room_models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from . import models
from django.http import Http404


class CreateError(Exception):
    pass


def create(request, room, year, month, day):
    try:
        date_obj = datetime.datetime(year, month, day)
        room = room_models.Room.objects.get(pk=room)
        models.BookedDay.objects.get(day=date_obj, reservation__room=room)
        raise CreateError()
    except (room_models.Room.DoesNotExist, CreateError):
        messages.error(request, "Cant Reserve Room")
        return redirect(reverse("core:home"))
    except models.BookedDay.DoesNotExist:
        reservation = models.Reservation.objects.create(
            guest=request.user,
            room=room,
            check_in=date_obj,
            check_out=date_obj + datetime.timedelta(days=1),
        )
        return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))


class ReservationDetailView(View):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        reservation = models.Reservation.objects.get(pk=pk)
        if not reservation or (
            reservation.guest != self.request.user
            and reservation.room.host != self.request.user
        ):
            raise Http404()
        return render(
            self.request, "reservations/detail.html", {"reservation": reservation}
        )
