from django.urls import path
from . import views

app_name = "lists"
urlpatterns = [
    path("lists/<int:room_pk>", views.save_room, name="save_room"),
]
