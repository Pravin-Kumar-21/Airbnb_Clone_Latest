from django.urls import path
from rooms import views as room_views
from users import views as user_views

app_name = "core"
urlpatterns = [
    path("", room_views.HomeView.as_view(), name="home"),
    path("login/", user_views.LoginView.as_view(), name="vialogin"),
]
