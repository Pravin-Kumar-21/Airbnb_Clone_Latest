from django.urls import path
from . import views

app_name = "rooms"
urlpatterns = [
    path("<int:pk>", views.RoomDetail.as_view(), name="detail"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("<int:pk>/edit/", views.EditRoomView.as_view(), name="edit"),
    path("<int:pk>/photos/", views.RoomPhotosView.as_view(), name="photos"),
    path("<int:pk>/photos/add", views.AddPhotoView.as_view(), name="add_photos"),
    path(
        "<int:room_pk>/photos/<int:photo_pk>/delete/",
        views.delete_photo,
        name="delete_photo",
    ),
    path(
        "<int:room_pk>/photos/<int:photo_pk>/edit/",
        views.EditPhotoView.as_view(),
        name="edit_photo",
    ),
    path("create/", views.CreateRoomView.as_view(), name="create_room"),
]
