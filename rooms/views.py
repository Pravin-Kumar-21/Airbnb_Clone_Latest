from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def all_rooms(request):
    now = datetime.now()
    hungry = True
    return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
