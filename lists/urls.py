from django.urls import path
from . import views

app_name = "lists"
urlpatterns = [
    path("toggle/<int:room_pk>", views.toggle_room, name="toggle_room"),
    path("favourites/ ", views.my_favourites.as_view(), name="favourites"),
]
