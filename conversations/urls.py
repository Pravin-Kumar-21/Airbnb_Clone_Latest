from django.urls import path
from . import views

app_name = "conversations"

urlpatterns = [
    path("go/<int:a_pk>/<int:b_pk>", views.go_converstion, name="go"),  # type: ignore
    path("<int:pk>/", views.ConversationDetailView.as_view(), name="detail"),
]
